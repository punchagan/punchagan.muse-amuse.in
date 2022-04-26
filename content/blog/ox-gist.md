---
title: "GitHub Gists from Emacs Orgmode"
description: "I released my first Emacs MELPA package -- [[https://melpa.org/#/ox-gist][ox-gist]] -- An Orgmode backend to export and update sub-trees and buffers to GitHub gists."
date: 2022-04-26T12:37:00+05:30
tags: ["blag", "emacs", "github", "hack", "programming", "orgmode"]
draft: false
---

TL;DR: I released my first Emacs MELPA package -- [ox-gist](https://melpa.org/#/ox-gist) -- An Orgmode backend
to export and update sub-trees and buffers to GitHub gists.  It was a great
experience contributing to MELPA.


## Motivation {#motivation}

I often share bits and pieces of my `journal.org` file with others, mostly for
reading, some times for comments. The file contains different subtrees for each
day with subtrees for different topics, meetings, articles, etc.

Orgmode lets you export subtrees to specific file names using the
`EXPORT_FILE_NAME` property (and `FILE_NAME` buffer export option when
exporting full buffers). It is easy to create these exported files on a
publicly accessible webserver using the power of [Emacs TRAMP mode](https://www.gnu.org/software/tramp/).  For
instance, I often set the property to some thing like
`/ssh:muse-amuse.in:~/public_html/<filename>` to publish stuff.

But, exporting to HTML is a distraction some times because I start fiddling
with CSS and styling. Exporting to a simple org file doesn't seem to cut it
because there's no styling at all, and making longer exports hard to read in a
web-browser.  Exporting to a GitHub Gist is a nice middle ground because GitHub
renders Orgmode files reasonably well. Additionally, the comment functionality
is pretty handy.

I could also directly use [@defunkt](https://github.com/defunkt/)'s excellent [`gist.el`](https://github.com/defunkt/gist.el) to share stuff as
Gists.  I've used it in the past, and it works well when I don't care about
having the contents of the Gist locally on my machine. It's also quite easy to
update existing/old Gists in this scenario, since there's a single "source of
truth" and `gist.el` makes it quite easy to update Gists.

But, this isn't good enough when I want to have a "synced" copy of the text on
my machine.  Also, it doesn't work very well when I want to share just a
subtree from my notes file, and not the entire file.  I've to export the
subtree to a temporary Orgmode buffer and then create a Gist from that buffer.


## Hackish wrapper around `gist.el` {#hackish-wrapper-around-gist-dot-el}

A couple or so years ago, I wrote a wrapper around `gist.el` to let me post
Orgmode subtrees as a Gist and also update them when I edited these subtrees
locally.  There was no support for exporting entire buffers since that wasn't
my use-case.  This wrapper code was just a part of my `.emacs` and worked
reasonably well for me.

A few weeks ago, I ended up procrastinating on writing and sharing notes for a
discussion with a friend, and extracted this wrapper as a separate package --
`org2gist` -- to make it easy for other people to use.


## MELPA submission and feedback {#melpa-submission-and-feedback}

I [submitted](https://github.com/melpa/melpa/pull/7940) this as a package to [MELPA](https://melpa.org/) while being skeptical about whether it
would be accepted.  I wasn't sure if my thin wrapper around `gist.el` would
meet MELPA's criteria for a "Reasonably innovative package":

> MELPA provides a curated set of Emacs Lisp packages, not an exhaustive list
> of every single Emacs Lisp file ever created. By default, MELPA maintainers
> will reject packages that duplicate functionality provided by existing
> packages. Please try to improve existing packages instead of creating new
> ones when possible.

It was a pleasant surprise to get very helpful reviews from the MELPA
maintainers.  They not only thought the package was good enough to include in
MELPA, but also looked at it's code and gave great feedback --- not just basic
quality checks before accepting the package into MELPA.

I'm pretty sure mainting a package repository like MELPA is a lot of work, but
as an end-user it mostly just worked for me and I never really gave it much
thought.  It was eye-opening to submit the package to MELPA and see first-hand
the care and effort the maintainers put into what goes into the repository.

[@riscy](https://github.com/riscy/) (a MELPA maintainer) [suggested](https://github.com/melpa/melpa/pull/7940#issuecomment-1080036663) a different approach that I hadn't
thought of --- turning the wrapper into an [Orgmode Export backend](https://orgmode.org/manual/Exporting.html).


## Current version: `ox-gist` {#current-version-ox-gist}

It turned out to be a great idea which I ended up implementing.  The user
interface became much cleaner, since it used the Orgmode Export UI.  And it
also forced me to "complete" the feature-set by adding support for exporting
entire Orgmode buffers to GitHub Gists, not just subtrees.

The package now adds an Orgmode export backend that lets you export a subtree
or the whole buffer as a GitHub Gist, similar to how you'd export to HTML or
LaTeX from Orgmode. The GitHub Gist ID is saved for each exported buffer or
subtree and is to update a Gist when re-exporting an already exported subtree
or buffer.


## Outro {#outro}

The package has now been added to MELPA as [`ox-gist`](https://github.com/punchagan/ox-gist).  Feel free to give it a
spin and give feedback directly to me or on the [issue tracker](https://github.com/punchagan/ox-gist/issues)!

I don't know if anyone else would find the package useful and use it, though,
MELPA tells me that 20-odd people atleast downloaded it.  I'm happy this code
may be to a handful of people.

Also, I now have a new found appreciation for MELPA and the work put into it by
the maintainers.  I'm glad I took the time out to submit this package to MELPA.

<div style="font-size:small;" class="reviewers">

Thanks to [Shantanu](http://baali.muse-amuse.in) for reading drafts and helping me restructure this post.

</div>
