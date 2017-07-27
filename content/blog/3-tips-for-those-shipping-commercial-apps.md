+++
title = "3 tips for those shipping (commercial) apps"
date = "2012-11-28T00:00:00+05:30"
tags = ["enthought", "programming", "software", "tips"]
draft = false
+++

Here are some very generic (and paraphrased) notes from a short
talk today, by Deepankar Sharma.

1.  Whenever you release a new major version, make sure you keep a
    copy of the whole "ecosystem" to be able to run it whenever you
    want.  At any point in time, you should be able to run any
    version of your software.
2.  When writing benchmarks/tests/etc., try and ensure that you
    cover a broad spectrum of test data, to try and replicate the
    different types of data that users could possibly have.
3.  Don't develop applications with modes.  Be very careful before
    you add a new mode to your application, effectively adding one
    more code path to maintain.
4.  (Bonus) Beware of too much extensibility
