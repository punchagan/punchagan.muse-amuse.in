---
title : "Recurse Center, 2014-07-11"
date : 2014-07-13T19:09:29-04:00
tags : ["python"]
categories : ["recursecenter"]
draft : false
---

-   I didn't spend much time at Hacker School on Friday.  I reached a bit late
    for the start of "Recursion day", and did a few problems.  The problems were
    simple, but interesting.  After lunch, I headed home to start to Philly.
-   Later in the day, I did some refactoring of the code to have the index reader
    and writer split out.
-   I also added a setup.py to be able to install the package using the standard
    tools instead of PYTHONPATH hacks and stuff.
-   During the refactoring, I again hit [this bug](./posts/an-import-gotcha-in-python.html).  I found out from Pankaj that
    he has `from __future__ import print_function, absolute_imports` at the start
    of his files these days.  I think I'm going to do it, too.


## Saturday & Sunday {#saturday-and-sunday}

-   I didn't do much during the weekend. I ended up adding a TXT record for SPF
    for this domain, to work around Gmail marking bulk mails for the
    [childrens-park](http://github.com/punchagan/childrens-park) newsletter as spam. I was able to send one newsletter, but not
    sure if only the SPF is enough or I'll have to setup DKIM, and other stuff.
    (I don't understand most of these acronyms!)

-   Someone mentioned <http://github.com/kennethreitz/autoenv> on Zulip, and I
    really liked the idea.  I have started using it for a couple of projects and
    also got rid of a couple of my bashrc aliases, and created a new [project](https://github.com/punchagan/home-bin/blob/master/project)
    command with completions of the directories in my project directory.  I like
    this setup, as of now.
