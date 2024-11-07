#!/bin/bash
set -ex

PUBLIC_DIR="public"
DRAFTS_DIR="drafts"
GIT_URL=$(git remote get-url origin)

# Ensure theme is using our local changes
set +e
grep theme.*\"er\" config.toml
USING_ER_THEME=$?
set -e
if [ $USING_ER_THEME -eq 0 ]; then
    grep -q develop themes/er/.git/HEAD
fi

pushd "$(dirname "${0}")"
# Publish the site (along with drafts)
./hugo.sh --cleanDestinationDir -D -d "${DRAFTS_DIR}"
mkdir -p "${DRAFTS_DIR}/drafts"  # Ensure dir exists, even if no draft posts
# Publish the site *without* drafts
./hugo.sh --cleanDestinationDir -d "${PUBLIC_DIR}"
cp -a "${DRAFTS_DIR}/drafts" "${PUBLIC_DIR}"
rm -r "${DRAFTS_DIR}"

# Push to GitHub
pushd "${PUBLIC_DIR}"
git init
git add .
git commit -m "Deploy to GitHub Pages" || true
git show --stat --oneline
read -rp "Are you sure you want to publish these changes? [y/N] " answer
case $answer in
    [yY]* ) echo "Okay, running the deploy....";
            git push --force "${GIT_URL}" main:gh-pages;;

    * )     echo "Not deploying...";;
esac
popd

popd
