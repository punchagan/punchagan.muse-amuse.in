#!/bin/bash
set -ex

# Ensure themes repo is setup

DIR=$PWD
mkdir -p themes
cd themes/
if [ ! -d "er" ]; then
    git clone git@github.com:punchagan/er.git
fi

cd er/
git checkout develop

cd "${DIR}"
git remote remove origin
git remote add origin muse-amuse.in:~/repos/muse-amuse.in.git
git remote set-url --add --push origin muse-amuse.in:~/repos/muse-amuse.in.git
git remote set-url --add --push origin "git@github.com:punchagan/punchagan.muse-amuse.in.git"
