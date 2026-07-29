#!/usr/bin/env bash

set -euo pipefail

# Specify the version of Pagefind you want
PAGEFIND_VERSION="1.5.2"  # Freeze pagefind version to avoid breakages!

PAGEFIND_BIN_DIR="./bin"
PAGEFIND_BIN="$PAGEFIND_BIN_DIR/pagefind"

# Create the bin directory if it doesn't exist
mkdir -p "$PAGEFIND_BIN_DIR"

# macOS doesn't ship sha256sum by default (BSD userland), but does have
# shasum - fall back to that instead of hard-requiring coreutils.
sha256_of() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print $1}'
    else
        shasum -a 256 "$1" | awk '{print $1}'
    fi
}

# Function to download Pagefind
download_pagefind() {
    echo "Downloading Pagefind version $PAGEFIND_VERSION..."
    PLATFORM=$(uname -s)
    ARCH=$(uname -m)

    # Map to the Rust target triples used in Pagefind's release assets
    case "$PLATFORM" in
        Linux) TARGET="unknown-linux-musl" ;;
        Darwin) TARGET="apple-darwin" ;;
        *) echo "Unsupported platform: $PLATFORM" >&2; exit 1 ;;
    esac

    case "$ARCH" in
        x86_64) TARGET="x86_64-$TARGET" ;;
        arm64|aarch64) TARGET="aarch64-$TARGET" ;;
        *) echo "Unsupported architecture: $ARCH" >&2; exit 1 ;;
    esac

    ARCHIVE_NAME="pagefind-v${PAGEFIND_VERSION}-${TARGET}.tar.gz"
    DOWNLOAD_URL="https://github.com/Pagefind/pagefind/releases/download/v$PAGEFIND_VERSION/${ARCHIVE_NAME}"

    echo "Download location: $DOWNLOAD_URL"
    curl -L "$DOWNLOAD_URL" -o "$PAGEFIND_BIN_DIR/pagefind.tar.gz"

    # Each release asset has its own ".sha256" sidecar file (sha256sum
    # format: "<hash>  <filename>").
    EXPECTED_SHA=$(curl -sL "${DOWNLOAD_URL}.sha256" | awk '{print $1}')
    if [ -z "$EXPECTED_SHA" ]; then
        echo "Could not fetch a checksum for ${ARCHIVE_NAME} - aborting." >&2
        rm -f "$PAGEFIND_BIN_DIR/pagefind.tar.gz"
        exit 1
    fi
    ACTUAL_SHA=$(sha256_of "$PAGEFIND_BIN_DIR/pagefind.tar.gz")
    if [ "$EXPECTED_SHA" != "$ACTUAL_SHA" ]; then
        echo "Checksum mismatch for ${ARCHIVE_NAME}: expected $EXPECTED_SHA, got $ACTUAL_SHA - aborting." >&2
        rm -f "$PAGEFIND_BIN_DIR/pagefind.tar.gz"
        exit 1
    fi

    tar -xzf "$PAGEFIND_BIN_DIR/pagefind.tar.gz" -C "$PAGEFIND_BIN_DIR"
    rm "$PAGEFIND_BIN_DIR/pagefind.tar.gz"
    chmod +x "$PAGEFIND_BIN"

    echo "Pagefind version $PAGEFIND_VERSION is now installed at $PAGEFIND_BIN_DIR."
}

# Check if Pagefind is already installed and matches the specified version
if [ -f "$PAGEFIND_BIN" ]; then
    INSTALLED_VERSION=$("$PAGEFIND_BIN" --version | awk '{print $2}' | tr -d 'v')

    if [ "$INSTALLED_VERSION" == "$PAGEFIND_VERSION" ]; then
        echo "Using Pagefind version $PAGEFIND_VERSION ..."
    else
        echo "A different version of Pagefind is installed (version $INSTALLED_VERSION). Replacing it with version $PAGEFIND_VERSION."
        download_pagefind
    fi
else
    echo "Pagefind is not installed. Downloading version $PAGEFIND_VERSION..."
    download_pagefind
fi

"${PAGEFIND_BIN}" "$@"
