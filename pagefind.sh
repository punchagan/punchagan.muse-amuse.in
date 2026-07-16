#!/usr/bin/env bash

set -euo pipefail

# Specify the version of Pagefind you want
PAGEFIND_VERSION="1.5.2"  # Freeze pagefind version to avoid breakages!

PAGEFIND_BIN_DIR="./bin"
PAGEFIND_BIN="$PAGEFIND_BIN_DIR/pagefind"

# Create the bin directory if it doesn't exist
mkdir -p "$PAGEFIND_BIN_DIR"

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

    DOWNLOAD_URL="https://github.com/Pagefind/pagefind/releases/download/v$PAGEFIND_VERSION/pagefind-v${PAGEFIND_VERSION}-${TARGET}.tar.gz"

    echo "Download location: $DOWNLOAD_URL"
    curl -L "$DOWNLOAD_URL" -o "$PAGEFIND_BIN_DIR/pagefind.tar.gz"
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
