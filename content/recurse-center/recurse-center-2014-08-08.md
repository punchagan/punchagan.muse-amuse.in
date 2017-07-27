+++
title = "Recurse Center, 2014-08-08"
date = 2014-08-09T20:56:22-04:00
tags = ["chrome", "emacs", "python"]
categories = ["recursecenter"]
draft = false
+++

-   I spent the morning doing some white-boarding interview practice with a Jorge
    and Brian.
-   I spent the rest of the day, playing with PyPy and working through [a tutorial](http://morepypy.blogspot.in/2011/04/tutorial-writing-interpreter-with-pypy.html)
    that teaches us to write a BF interpreter.
-   I spent the Saturday revamping my Emacs config.  The main issue with my
    config was having a "package" list, of all the packages that the
    configuration uses, in case we are trying to duplicate it elsewhere.  I
    noticed that this gets out of sync, because I install packages by hand and
    never update this list.  I wrote up [some code](https://github.com/punchagan/dot-emacs/blob/master/user-lisp/setup-defuns.el), that keeps this list in sync
    with all the packages I have installed.  I configured el-get to play well
    with my config, and am pretty happy with my setup, though I still have to add
    some matching/searching features with helm/ido/whatever else.
-   I spent the Sunday writing a patch to [xtab](https://github.com/punchagan/xtab/tree/kill-by-memory) to be able to limit the number of
    tabs in Chromium by the memory it uses.
