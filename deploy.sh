#!/bin/bash
set -e

PUBLIC_DIR="public"
DEV_DIR="dev"
DRAFTS="${PUBLIC_DIR}/drafts"

GIT_URL=$(git remote get-url origin)

# Build the site
pushd $(dirname $0)
rm -rf "${PUBLIC_DIR}"
rm -rf "${DEV_DIR}"
hugo
# Build drafts to dev dir
hugo -D -d "${DEV_DIR}"

# Copy drafts to drafts/ dir
mkdir -p "${DRAFTS}"
for d in $(diff <(cd dev/ && find . -type d) <(cd public && find . -type "d")|grep "<"|cut -d " " -f 2); do
    echo "${DEV_DIR}/${d}"
    cp -a "${DEV_DIR}/${d}" "${DRAFTS}"
done

# Push to GitHub
pushd "${PUBLIC_DIR}"
git init
git add .
git commit -m "Deploy to GitHub Pages"
git push --force "${GIT_URL}" master:gh-pages
popd

popd
