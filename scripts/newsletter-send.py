#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "html2text"]
# ///
"""Build this week's digest and send it as a Resend broadcast.

Run it from anywhere; it operates on the repo it lives in. Meant to be run
either by hand after ./scripts/deploy.sh, or on a schedule via
.github/workflows/newsletter.yml - missing a week or occasionally sending
twice is acceptable here, so there's deliberately no locking or retry
logic.

Subscribers sign up via a Google Form; responses land in a Sheet shared
"anyone with the link" (viewer), so no service account is needed - just
the CSV export endpoint. Column A is always the Form's own submission
timestamp; whichever other column looks like an email address is taken as
the subscriber's address, so it doesn't matter how many other questions
are on the Form or what order they're in.

Sync only runs on an actual send (after the empty-digest and --dry-run
early exits), reusing last_sent as the cutoff for "new rows" too - not a
separate marker. That means it does nothing during a quiet week with no
new posts, which is fine: broadcasts go out to whoever's in the segment
at send time, not at signup time, so a subscriber ends up in the same
first digest either way, however late their Resend contact gets created.

Every row newer than last_sent gets explicitly upserted with
unsubscribed=False - deliberately, not by omission - so refilling the
form is how someone resubscribes after unsubscribing via Resend's own
link. A row that's never resubmitted is never revisited, so an
unsubscribe always stays put.

    ./scripts/newsletter-send.py --dry-run   # build + preview, no API calls
    ./scripts/newsletter-send.py             # build, sync, create broadcast, send (asks to confirm)
    ./scripts/newsletter-send.py --yes       # same, but sends without asking (for CI)

Expects RESEND_API_KEY, RESEND_SEGMENT_ID, RESEND_FROM and GOOGLE_SHEET_ID
already in the environment - via .envrc (gitignored, direnv) locally, or
via a workflow's secrets: -> env: mapping in CI. Nothing here cares which.

Run directly (the uv shebang resolves and installs `requests` into an
ephemeral venv on first run - no manual pip install/venv setup needed):

    ./scripts/newsletter-send.py --dry-run
"""

import csv
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import html2text
import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWSLETTER_JSON = REPO_ROOT / "data" / "newsletter.json"
UNSUBSCRIBE_PLACEHOLDER = "https://unsubscribe.invalid/"
UNSUBSCRIBE_MERGE_TAG = "{{{RESEND_UNSUBSCRIBE_URL}}}"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
# Google Forms' own timestamp column, as observed - not locale-proof, but
# explicit and no longer guessed by a C library the way `date -d` was.
FORM_TIMESTAMP_FORMAT = "%m/%d/%Y %H:%M:%S"


def read_last_sent() -> str:
    return json.loads(NEWSLETTER_JSON.read_text())["last_sent"]


def write_last_sent(value: str) -> None:
    data = json.loads(NEWSLETTER_JSON.read_text())
    data["last_sent"] = value
    NEWSLETTER_JSON.write_text(json.dumps(data, indent=2) + "\n")


def require_env(names: list[str]) -> dict[str, str]:
    env = {}
    missing = []
    for name in names:
        value = os.environ.get(name, "")
        if not value:
            missing.append(name)
        env[name] = value
    if missing:
        for name in missing:
            print(f"{name} is not set - see .envrc", file=sys.stderr)
        sys.exit(1)
    return env


def resend(session: requests.Session, method: str, path: str, body: dict | None = None) -> requests.Response:
    return session.request(method, f"https://api.resend.com{path}", json=body)


def build_digest(dry_run: bool) -> dict | None:
    print("Building digest...")
    with tempfile.TemporaryDirectory() as build_dir:
        subprocess.run(
            ["./hugo.sh", "--config", "config.toml,config-newsletter.toml", "-d", build_dir],
            cwd=REPO_ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        digest_path = Path(build_dir) / "newsletter.json"
        # Hugo writes no file at all when the template renders empty, so a
        # missing file and an empty one both mean "nothing new since last_sent".
        if not digest_path.exists() or digest_path.stat().st_size == 0:
            print(f"Nothing new since {read_last_sent()} - not sending.")
            return None
        digest = json.loads(digest_path.read_text())

    print(f"Subject: {digest['subject']}")
    # Swap the placeholder for Resend's merge tag; it can't be written
    # directly in the Hugo template (Go's href autoescaping mangles the
    # braces).
    digest["html"] = digest["html"].replace(UNSUBSCRIBE_PLACEHOLDER, UNSUBSCRIBE_MERGE_TAG)

    # A plain-text alternative alongside the HTML - multipart emails tend to
    # score better with spam filters than HTML-only. Converted from the
    # rendered HTML (not raw markdown, which would leave literal **/[]()
    # syntax in it) so links survive as "text (url)" instead of Hugo's
    # .Plain, which would strip the href and keep only the anchor text.
    converter = html2text.HTML2Text()
    converter.body_width = 0  # don't hard-wrap - let email clients do it
    digest["text"] = converter.handle(digest["html"])

    if dry_run:
        preview = REPO_ROOT / "public" / "newsletter-preview.html"
        preview.parent.mkdir(parents=True, exist_ok=True)
        preview.write_text(digest["html"])
        preview.with_suffix(".txt").write_text(digest["text"])
        print(f"Dry run - wrote preview to {preview} (and .txt), no API calls made.")
        return None

    return digest


def fetch_sheet_csv(sheet_id: str) -> str:
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    resp = requests.get(url)  # follows redirects by default
    if not resp.ok or "," not in resp.text.splitlines()[0]:
        print(f"Failed to fetch the signup sheet as CSV (HTTP {resp.status_code}). Got:", file=sys.stderr)
        print("\n".join(resp.text.splitlines()[:5]), file=sys.stderr)
        sys.exit(1)
    return resp.text


def sync_subscribers(session: requests.Session, env: dict[str, str]) -> int:
    print("Syncing subscribers...")
    csv_text = fetch_sheet_csv(env["GOOGLE_SHEET_ID"])

    cutoff = datetime.fromisoformat(read_last_sent()).replace(tzinfo=None)
    synced = 0

    for row in csv.reader(io.StringIO(csv_text)):
        if not row:
            continue
        ts, rest = row[0], row[1:]

        if ts == "Timestamp":
            print(f"  header: {row}", file=sys.stderr)
            continue

        # Column A is always the Form's own timestamp, but which column
        # holds the email address depends on however many other questions
        # are on the Form (Name, etc.) and in what order - so find it by
        # shape, not by a fixed position that breaks the moment the Form
        # changes.
        email = next((f for f in rest if EMAIL_RE.match(f)), None)
        if email is None:
            print(f"  skip (no email-shaped field): ts=[{ts}] fields={rest}", file=sys.stderr)
            continue

        try:
            row_time = datetime.strptime(ts, FORM_TIMESTAMP_FORMAT)
        except ValueError:
            row_time = None
        if row_time is None or row_time <= cutoff:
            print(f"  skip (too old): ts=[{ts}] email={email}", file=sys.stderr)
            continue

        print(f"  syncing: {email} (ts={ts})", file=sys.stderr)

        # Try updating an existing contact first (this is the resubscribe
        # path - unsubscribed is set explicitly, never left to whatever an
        # unspecified field would default to); fall back to creating a new
        # one.
        resp = resend(session, "PATCH", f"/contacts/{email}", {"unsubscribed": False})
        if resp.status_code != 200:
            resend(
                session,
                "POST",
                "/contacts",
                {
                    "email": email,
                    "unsubscribed": False,
                    "segments": [{"id": env["RESEND_SEGMENT_ID"]}],
                },
            )
        synced += 1

    print(f"Synced {synced} subscriber row(s).")
    return synced


def create_and_send_broadcast(
    session: requests.Session, env: dict[str, str], digest: dict, auto_confirm: bool
) -> None:
    print("Creating broadcast...")
    resp = resend(
        session,
        "POST",
        "/broadcasts",
        {
            "segment_id": env["RESEND_SEGMENT_ID"],
            "from": env["RESEND_FROM"],
            "subject": digest["subject"],
            # "name" is purely a dashboard label ("internal reference" per
            # Resend's docs), separate from the subject line recipients see -
            # reusing the same string just means broadcasts are easy to find
            # in the list by the same name subscribers saw.
            "name": digest["subject"],
            "html": digest["html"],
            "text": digest["text"],
        },
    )
    broadcast_id = resp.json().get("id") if resp.ok else None
    if not broadcast_id:
        print("Failed to create broadcast. Resend said:", file=sys.stderr)
        print(resp.text, file=sys.stderr)
        sys.exit(1)

    print(f"Created broadcast {broadcast_id} (check the Audience has the right subscribers before confirming).")
    if auto_confirm:
        print("--yes passed, sending without prompting.")
    else:
        answer = input("Send it? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            print(f"Not sending. Broadcast {broadcast_id} is saved as a draft in Resend.")
            return

    resp = resend(session, "POST", f"/broadcasts/{broadcast_id}/send")
    # A successful send echoes the same broadcast id back.
    if not resp.ok or resp.json().get("id") != broadcast_id:
        print("Failed to send broadcast. Resend said:", file=sys.stderr)
        print(resp.text, file=sys.stderr)
        sys.exit(1)

    print("Sent.")

    # Only after a successful send, so a failure part-way through just
    # means the same posts go out next run.
    sent_at = datetime.now().astimezone().isoformat()
    write_last_sent(sent_at)
    print(f"Updated {NEWSLETTER_JSON.relative_to(REPO_ROOT)} last_sent to {sent_at} - commit it.")


def main() -> None:
    dry_run = "--dry-run" in sys.argv[1:]
    # For CI (GitHub Actions) - there's no stdin to prompt on. Interactive
    # runs always still get the confirmation; this only skips it when
    # explicitly asked to.
    auto_confirm = "--yes" in sys.argv[1:]

    # Credentials are only needed for a real send - a dry run builds and
    # previews the digest without touching Resend.
    env = {} if dry_run else require_env(
        ["RESEND_API_KEY", "RESEND_SEGMENT_ID", "RESEND_FROM", "GOOGLE_SHEET_ID"]
    )

    digest = build_digest(dry_run)
    if digest is None:
        return

    with requests.Session() as session:
        if not dry_run:
            session.headers.update(
                {
                    "Authorization": f"Bearer {env['RESEND_API_KEY']}",
                    "Content-Type": "application/json",
                }
            )
        sync_subscribers(session, env)
        create_and_send_broadcast(session, env, digest, auto_confirm)


if __name__ == "__main__":
    main()
