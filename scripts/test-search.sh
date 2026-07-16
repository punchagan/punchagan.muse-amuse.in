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
python3 -m http.server "$PORT"
