#!/usr/bin/env bash

set -euo pipefail

# Specify the version of Hugo you want
HUGO_VERSION="0.138.0"  # Freeze hugo version to avoid breakages!

HUGO_BIN_DIR="./bin"
HUGO_BIN="$HUGO_BIN_DIR/hugo"

# Create the bin directory if it doesn't exist
mkdir -p "$HUGO_BIN_DIR"

# Function to download Hugo
download_hugo() {
    echo "Downloading Hugo version $HUGO_VERSION..."
    PLATFORM=$(uname -s | tr '[:upper:]' '[:lower:]')
    ARCH=$(uname -m)

    # Adjust architecture naming
    if [ "$ARCH" == "x86_64" ]; then
        ARCH="amd64"
    elif [[ "$ARCH" == "arm"* ]]; then
        ARCH="arm"
    elif [[ "$ARCH" == "aarch64" ]]; then
        ARCH="arm64"
    fi

    DOWNLOAD_URL="https://github.com/gohugoio/hugo/releases/download/v$HUGO_VERSION/hugo_extended_${HUGO_VERSION}_${PLATFORM}-${ARCH}.tar.gz"

    echo "Download location: $DOWNLOAD_URL"
    # Download and extract Hugo
    curl -L "$DOWNLOAD_URL" -o "$HUGO_BIN_DIR/hugo.tar.gz"
    tar -xzf "$HUGO_BIN_DIR/hugo.tar.gz" -C "$HUGO_BIN_DIR"
    rm "$HUGO_BIN_DIR/hugo.tar.gz"
    chmod +x "$HUGO_BIN"

    echo "Hugo version $HUGO_VERSION is now installed at $HUGO_BIN_DIR."
}

# Check if Hugo is already installed and matches the specified version
if [ -f "$HUGO_BIN" ]; then
    INSTALLED_VERSION=$("$HUGO_BIN" version | awk '{print $2}' | tr -d 'v' | sed 's/-.*//')

    if [ "$INSTALLED_VERSION" == "$HUGO_VERSION" ]; then
        echo "Using Hugo version $HUGO_VERSION ..."
    else
        echo "A different version of Hugo is installed (version $INSTALLED_VERSION). Replacing it with version $HUGO_VERSION."
        download_hugo
    fi
else
    echo "Hugo is not installed. Downloading version $HUGO_VERSION..."
    download_hugo
fi

"${HUGO_BIN}" "$@"
