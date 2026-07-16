#!/usr/bin/env bash

# Builds the site, indexes it with Pagefind, and serves it statically so
# search can actually be tested locally. `hugo server` alone can't do this -
# it doesn't produce a real public/ directory for pagefind.sh to index.
#
# Mirrors what deploy.sh does in production: builds without drafts, indexes
# that, so what you see here matches what search will find once deployed.

set -euo pipefail

PORT="${1:-8899}"
BUILD_DIR="$(mktemp -d)"

trap 'rm -rf "$BUILD_DIR"' EXIT

cd "$(dirname "${0}")/.."

./hugo.sh --cleanDestinationDir -d "$BUILD_DIR" --baseURL "http://127.0.0.1:${PORT}/"
./pagefind.sh --site "$BUILD_DIR"

echo
echo "Serving at http://127.0.0.1:${PORT}/ - Ctrl+C to stop."
echo
cd "$BUILD_DIR"

# Plain `python3 -m http.server` doesn't emulate GitHub Pages' 404 fallback
# (serving 404.html, with a 404 status, while keeping the broken URL in the
# address bar) - it just returns its own generic error page. This custom
# handler does that, so the 404 page's Pagefind-based suggestions can
# actually be tested against a realistic broken URL.
python3 - "$PORT" << 'PYEOF'
import http.server
import os
import sys

PORT = int(sys.argv[1])


class NotFoundFallbackHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            for index in ("index.html", "index.htm"):
                if os.path.exists(os.path.join(path, index)):
                    return super().send_head()
        if not os.path.exists(path):
            with open("404.html", "rb") as f:
                content = f.read()
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return None
        return super().send_head()


http.server.test(HandlerClass=NotFoundFallbackHandler, port=PORT, bind="127.0.0.1")
PYEOF
