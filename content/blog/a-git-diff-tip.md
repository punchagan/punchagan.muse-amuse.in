+++
title = "A git-diff tip"
date = "2012-08-22T00:00:00+05:30"
tags = ["git", "version_control"]
draft = false
+++

One of the things with git that you can mess-up, if you are not
used to, is git diff.  A friend of mine was trying to add a couple
of new files, and changes to existing files.  But, he was on the
wrong branch, and wanted to change to a different branch, before
committing.  Being new to git, he wanted to take a patch.  Reset
the changes, apply the patch back.

This is what he did

```sh
git add new_file.txt
git add old_file1.txt old_file2.txt # don't add old_file3.txt
```

Oh, damn, I want to change the branch.

```sh
git diff > a.patch
git reset --hard
git checkout other-branch
```

Let me commit my changes...

```sh
git apply a.patch
git commit -m
git show
```

Oh crap!  Where are my new files?  They aren't commited!  Lemme
add them.

```sh
ls new_file.txt
ls: cannot access new_file.txt: No such file or directory
```

Dammit!  Where are my changes gone?

The problem was with `git diff`.  It gives only the only the
un-staged changes.  `--cached` option has to specified, to get the
staged changes in the diff output.  `git diff HEAD` shows diff
output with both staged and un-staged changes.

But the whole workflow above is a beginners workflow.  A user
comfortable with git would've committed and then moved the commit
around using cherry-pick or the like.

```sh
git add <all-files>
git commit -m "My awesome changes."  #committed on branch1
git checkout other-branch
git cherry-pick branch1
```
