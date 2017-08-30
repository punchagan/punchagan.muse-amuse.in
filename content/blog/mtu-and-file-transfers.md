---
title : "MTU and file transfers"
date : "2010-12-06T00:00:00+05:30"
tags : ["ssh"]
draft : false
---

A note to self, but may benefit someone facing a similar problem.

-   ****Problem**:** SSH-ing to our server was working well.  But, file
    transfers like `scp`, `git push` were failing.

-   ****Diagnosis**:** I had been thinking it was a problem with our
    campus network on the first night and was too
    sleepy to try and fix it.  But things didn't
    improve even after one full day.  Then I asked a
    friend of mine, and he confirmed that he has been
    facing the same problem for a couple of days.  I
    then tried file transfers to another server and
    it was working fine.  Then I tried file transfers
    between the two servers and even that worked fine!

-   ****Solution**:** After some googling, I figured that the problem
    was with a machine between me and the server.
    Changing the `mtu` to 1492 from 1500 on the
    server, fixed the problem. :)
