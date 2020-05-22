---
title: "My Favorite Git Resources"
description: "Git Resources that I really like, and have shared with friends over and over"
date: 2020-05-22T16:07:00+05:30
draft: false
---

I often help friends who are new to using `git` with using it. This blog post is
going to serve as a single link to share with them, instead of trying to find
individual links over and over.


## Understanding Git {#understanding-git}

I got started with using `git` after using `svn` and `hg` for a few months. But,
I would often be lost in the myriad of command line options, putting myself in
situations I couldn't come out of without some scars. I didn't really understand
how `git` worked, and that was the real problem.

Improving my mental model of how `git` works, and then trying to fit the
commands into this mental model is what made `git` finally click for me. The [Git
Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html) really helped me understand `git` from the inside out, and gave me a
much clearer mental model of `git`. There was no looking back from there.

If parables are not your thing, and you'd rather read something that takes a
less flowery and more straighforward approach to explaining these concepts, I
really liked John Wiegley's [Git from the Bottom Up](https://jwiegley.github.io/git-from-the-bottom-up/).


## Day-to-day git {#day-to-day-git}

[Zulip](https://zulipchat.com) (an open source group chat application that I spend a lot of time
contributing to) uses a rebase-heavy workflow, where good commits are merged
from different PRs, as and when they are reviewed, instead of waiting for all
the commits in a PR to be good to be merged. Developers often have to pull from
branches that have been force-pushed to, rebase their commits, squash commits,
learn to change `git` history, etc.

Zulip's [Git Guide](https://zulip.readthedocs.io/en/latest/git/index.html) is top-class documentation that gives guidelines on using git
from a practical stand-point. A lot of new developers use it to get upto speed
with Zulip's workflow that involves a lot of things that I've seen devs who have
been using git for many years struggle with.

The section on [pull request workflow](https://zulip.readthedocs.io/en/latest/git/pull-requests.html) is quite helpful, and should work
reasonably well for contributing to other FOSS projects too.

I also like the sections with recipes for common [`git` history edit actions](https://zulip.readthedocs.io/en/latest/git/fixing-commits.html), and
the [troubleshooting section](https://zulip.readthedocs.io/en/latest/git/troubleshooting.html) with recipes to get out of common troublesome
situations. [Oh shit, git!](https://ohshitgit.com/#accidental-commit-master) is a very similar resource to this, that has a bunch
of useful "recipes" to recover from different scenarios.

Julia Evans's [exercises](https://jvns.ca/blog/2019/08/30/git-exercises--navigate-a-repository/) approach to learning to explore a `git` repository is
quite interesting, though I haven't run through all the exercises myself.


## Git as a communication tool {#git-as-a-communication-tool}

I like to look at `git` history as telling the story of evolution of a code
base. The advice that is sometimes given to writers about doing the hardwork, so
that the readers can do less of it, holds true for git history too. Communicate
the story as clearly as possible for your readers to understand, and don't just
publish a "stream of consciousness" piece.

What does this mean in practical terms, though?

I think editing git history to present a clearer story is completely acceptable.
If one tries a handful of different things, and then finally finds the solution
to do something, it's not necessary to have all the failed attempts as commits.
Just the final approach can be a commit/pull-request, while documenting the
other approaches the commit message or as a comment in the code, if that makes
sense.

Expect your collaborators (including future you) to look at not just older
versions of code, but the commit history for understanding how a piece of code
evolved, for undertsanding the history. Make your git [commit messages](https://zulip.readthedocs.io/en/latest/contributing/version-control.html#commit-messages) as useful
as you can. Writing a good summary line goes a long way in understanding a
change. In most cases a body would be useful to explain the how and the why of
the change, while the summary line explains the what.

I like this [commit discipline](https://zulip.readthedocs.io/en/latest/contributing/version-control.html#commit-discipline) that the Git project itself uses, and was adopted
by the Zulip project: "Each commit is a minimal coherent idea". Simply put, you
want each commit to be such that they can be can be deployed (and/or reverted by
itself), without depending on any other commits alongside them. You can read
more about what minimal and coherent mean in this context in the [Zulip
documentation](https://zulip.readthedocs.io/en/latest/contributing/version-control.html#commit-discipline).


## Tools for Git {#tools-for-git}

Some of the confusion in using `git` even after understanding how it works is
the inconsitent CLI API that it often exposes. There has been some work going
into this, to make this more consistent. But, using a nice client can help with
this. I use the excellent Emacs client for `git` called [`magit`](https://magit.vc/screenshots/). It is an
intuitive UI on top of `git`'s data model, that allows me to do things that I
commonly want to do, with just a few hot-keys, instead of typing out elaborate
recipes to do things. I highly recommend it, if you are an Emacs user.

It is also helpful to change you shell's prompt to tell you more about the
status of the current directory's repository. There are a bunch of
configurations out there (Stackoverflow, Gists, etc.) that let you do this. The
git repo itself comes with a [prompt customisation](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh). I like being able to see at
least the current branch and dirty/clean state of the repo.

Here are some simple changes to the global `git` config, off the top of my head.
These could make your `git` workflow more pleasant.

```gitconfig
[push]
	# Push to the branch to the same remote branch as the one we are working on,
	# locally. This is the default in Git >= 2.0, so you may not need to set it.
	default = simple

[diff]
	# You could configure a GUI tool to use here. (I haven't used one in a long
	# time, and I don't have recommendations on what to use)
	tool = icdiff

[merge]
	# Shows common ancestor in a merge conflict. Makes it easier to understand
    # the conflict and merge, for me.
	conflictstyle = diff3

# Never garbage collect commits/blobs that are unreachable
# The cost of keeping this data around is negligble compared losing data
[gc]
	reflogExpire = never
	reflogExpireUnreachable = never
```


## Outro {#outro}

If you have other recommendations or tools that you'd like to share with me,
please do! Using `git` better, and understanding it better, is something that
I'm always excited about. I'd also be happy to answer questions, or help you
with specific things that you are trying to do with `git`.
