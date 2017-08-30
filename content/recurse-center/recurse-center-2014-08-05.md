---
title : "Recurse Center, 2014-08-05"
date : 2014-08-05T23:44:33-04:00
tags : ["nikola", "raspberry-pi"]
categories : ["recursecenter"]
draft : false
---

-   Spent a couple of hours in the morning, trying to revive a html template for
    blaggregator, that I missed out on committing previously, and wiped out due
    to negligence in using \`git clean\`.
-   Spent time post lunch working through the first two chapters of the baking pi
    course, by myself, reading up different references, and finally getting how
    I/O is mapped to the memory in ARM.
-   Actually, almost.  A variant of the example that I thought should work,
    doesn't.  So, I need to think/talk about it today.
-   I sent a patch to Nikola for the lastdeploy timestamp being UTC.  I was
    hoping to work around an [issue](https://github.com/sursh/blaggregator/issues/56) with Blaggregator, by somehow fixing it on the
    client side, but that's probably not the right way to go about it.
