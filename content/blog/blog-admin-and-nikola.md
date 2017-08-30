---
title : "blog-admin and Nikola"
date : "2016-05-21T00:00:00+05:30"
tags : ["blab", "blag", "blog", "emacs", "nikola"]
draft : false
---

Another post about blogging.

[blog-admin](https://github.com/CodeFalling/blog-admin) now supports [Nikola](http://getnikola.com), thanks to yours truly. `blog-admin` is an Emacs
package by [CodeFalling](https://twitter.com/codefalling) that lets you view and manage your (static site
generated) blog from within inside Emacs.

Nikola's command line utility is pretty nifty and does a bunch of useful
things. I had a few utility functions to do common tasks like create new post
and deploy blog. This worked well, but moment I came across this `blog-admin`'s
tabular view, I was sold!

[org2blog](https://github.com/punchagan/org2blog) (a blogging tool I used previously) had a tracking file that kept
track of all the posts I made, and I used it quite a bit for navigation --
thanks to `org-mode`'s search functionality. The tabular view of `blog-admin`
is even better!  I really like the fact that the author has tried to keep the
package generic enough to support any blog, and adding support for Nikola has
been quite easy.

The filtering functionality is crude, but good enough for a start. One thing I
want to add is a preview functionality for drafts. Showing some (writing)
statistics would also be nice -- No. posts in the last month, total published
posts, etc.  No promises, but you may see some of these things, soon. :)
