#!/bin/bash
set -ex

PUBLIC_DIR="public"
DRAFTS_DIR="drafts"
GIT_URL=$(git remote get-url origin)

pushd "$(dirname "${0}")/.."

# Refresh the (unused-by-the-build, reference-only) org copy of all posts
emacsclient -e "(pc/export-blog-posts)" || echo "Skipping blog-posts.org export - emacsclient unreachable"

# Ensure theme is using our local changes
set +e
grep theme.*\"er\" config.toml
USING_ER_THEME=$?
set -e
if [ $USING_ER_THEME -eq 0 ]; then
    grep -q develop themes/er/.git/HEAD
fi

# The newsletter's GitHub Action, and GitHub Pages itself, both build
# from origin's checked-out branch - not from this working tree. Make
# sure posts and assets actually make it there before deploying,
# otherwise the newsletter/site can silently diverge from what you
# think you just published.
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
git fetch origin "${CURRENT_BRANCH}"

set +e
git diff --quiet -- content static content-org
UNSTAGED=$?
git diff --cached --quiet -- content static content-org
STAGED=$?
set -e
UNTRACKED=$(git ls-files --others --exclude-standard -- content static content-org)

if [ $UNSTAGED -ne 0 ] || [ $STAGED -ne 0 ] || [ -n "${UNTRACKED}" ]; then
    echo "Uncommitted changes under content/, static/ or content-org/:"
    git status --short -- content static content-org
    read -rp "Commit these before deploying? [y/N] " answer
    case $answer in
        [yY]* )
            git add content static content-org
            git commit -m "Add/update posts and assets"
            ;;
        * )
            echo "Continuing without committing - anything left uncommitted here won't reach origin, so the newsletter cron and the live site can end up out of sync with what you're about to publish.";;
    esac
fi

AHEAD=$(git rev-list "origin/${CURRENT_BRANCH}..HEAD" -- content static content-org | wc -l)
if [ "${AHEAD}" -gt 0 ]; then
    echo "${AHEAD} commit(s) touching content/static/content-org not yet on origin/${CURRENT_BRANCH}:"
    git log --oneline "origin/${CURRENT_BRANCH}..HEAD" -- content static content-org
    read -rp "Push ${CURRENT_BRANCH} to origin now? [y/N] " push_answer
    case $push_answer in
        [yY]* ) git push origin "${CURRENT_BRANCH}";;
        * ) echo "Not pushing - the newsletter cron and site build won't see these until you do.";;
    esac
fi

# Publish the site (along with drafts)
./hugo.sh --cleanDestinationDir -D -d "${DRAFTS_DIR}"
mkdir -p "${DRAFTS_DIR}/drafts"  # Ensure dir exists, even if no draft posts
# Publish the site *without* drafts
./hugo.sh --cleanDestinationDir -d "${PUBLIC_DIR}"
# Index for search before copying drafts in, so drafts never end up searchable
./pagefind.sh --site "${PUBLIC_DIR}"
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
