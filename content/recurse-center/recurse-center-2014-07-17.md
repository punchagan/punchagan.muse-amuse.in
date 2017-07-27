+++
title = "Recurse Center, 2014-07-17"
date = 2014-07-19T16:45:12-04:00
tags = ["python", "raspberry_pi"]
categories = ["recursecenter"]
draft = false
+++

-   Kyle and I did a demo of our spectrum analyzer/visualizer during the
    presenations.  It was fun to work on, though we mostly just followed a
    tutorial on the web, and made use of a bunch of libraries.
-   I spent the night in HackerSchool.
-   I was cleaning up the code in the tutorial we were trying to follow.
-   Also, cleaned up the install.sh used by [lightshowpi](https://bitbucket.org/togiles/lightshowpi/src) project to not do all the
    ugly sudo setups, and use a Python virtualenv and install into that.
-   Refactored the ugly looking music part of the tutorial into a smaller script
    with only the functionality that we were going to use.
-   We hit an interesting bug that would light up all the LEDs on the strip, once
    in a while.  I didn't notice it during the night, because I had a "decay"
    factor (the max factor by which the height of the columns should get reduced
    between successive updates) was 0.9, but when the decay factor was reduced to
    a lower value, it would happen quite often.  Also, we didn't see this
    happening before.  So, we thought the bug was in the code I had written, when
    I should have been sleeping. After reading and debugging my code for a bit,
    with Kyle and Sean, I thought it was something hardware related that we were
    doing wrong.  But, it turns out that a library we were using lit-up the whole
    strip, when start and end values were both zero, instead of not lighting up
    anything!
-   Also, we hit another off-by one error, just before the demo. I didn't do the
    math for splitting the strip into columns too carefully, and we hadn't
    noticed the off-by one error until we taped up the strip into different
    columns on a pillar for demo.
-   There were some cool presentations by others.  I'll update the list on
    Monday, since I currently don't remember them all!  Looking at the list of
    names on the registration sheet would help!
-   The cleaned up code is [here](https://gist.github.com/punchagan/90a238fedabcd88ba512)
