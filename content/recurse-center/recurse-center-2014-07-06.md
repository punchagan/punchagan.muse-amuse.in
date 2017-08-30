---
title : "Recurse Center, 2014-07-06"
date : 2014-07-07T23:28:39-04:00
tags : ["code", "python"]
categories : ["recursecenter"]
draft : false
---

I took it easy during the weekend, and went on a nice camp with my a cousin's
family to TobyHanna State Park for a day or so, and spent the remaining (long)
weekend at their place in PA.  It was a pretty nice break!

Yesterday evening, I talked to Madhu about how ugly my code looked while I was
trying to use `libclang`, and he told me that he found a lot of wrapped C++/C
libraries end up being that way, and I also realized that using the Python AST
library seemed much cleaner, because it just contained Python objects, but
representing C/C++ objects in an AST and interacting with them in Python, isn't
that clean.

I cleaned up my code, and removed all the ugly regexes to use libclang to do
the parsing of the libs, and get the source code.  I basically got all the
tests passing, but they were taking an order of magnitude longer to run.  So, I
guess the next step is to cache things somehow.

I also added support for viewing the sources of built-in types.  It was pretty
simple, once I had everything working with libclang.
