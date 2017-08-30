---
title : "Recurse Center, 2014-06-19"
date : 2014-06-19T09:53:10-04:00
categories : ["recursecenter"]
draft : false
---

-   Yesterday was a bit more wandering than usual.  I still have to
    finish (actually, start) the last chapter in the UPenn course
    (Monads).  I hope to finish it during the weekend.

-   I started with reading [Typeclassopedia](http://www.haskell.org/haskellwiki/Typeclassopedia), in the hope of getting
    comfortable with Functors and Applicatives and to get introduced to
    Monads.  But, I got distracted before I got to the end of the part
    on Functors.

-   During the check-ins, Laura and Denise mentioned that they are both
    facing problems with OAuth, and would like to pair on it.  I decided
    to join them, since I've had reasonable luck with OAuth, though I
    knew I didn't understand it very well.  While they were working on
    getting it to work on OSX, I was trying to write a simple Python
    example to do it, and was getting a weird error about the
    `response_type` being not supported.  I was using [rauth](https://github.com/litl/rauth) in a way
    very similar to what I had done for [statiki](https://github.com/punchagan/statiki/blob/master/statiki.py#L49) but the Hacker School
    API server wasn't letting me through.  I could debug it only a
    little before lunch, and a little bit after lunch.  And realized
    that the `response_type` had to be one of `code` or `token` and not
    `json` or `empty`.  But this is a required parameter, and I expected
    `rauth` to do the right thing!  I got back to it at the end of the
    day, and went through the RFC for OAuth2 and wrote up a simple
    Python script to implement the whole thing, without using any 3rd
    party oauth libraries.  I think I understand the whole thing much
    better now, and will soon write up a blog post on it.

-   I spent about an hour or so on reviewing Nava's code (along with
    Tom, Amber and Patricia), that generated and solved mazes. We tried
    to make small incremental changes to her code, and improve it,
    hopefully giving her a sense of how to make the code more
    intentional.

-   Thursday evening presentations! People here have been working on
    such cool stuff!  Maze solvers and percolation probability
    calculators, phone gap based mobile applications, a cool Midi based
    music generator, an [emulator](https://github.com/mveytsman/emm-ess-pee) for MSP430 in Clojure, an event logger
    in ObjectiveC that can log to a web server and can be used by
    multiple clients to debug communication related issues, a HTTP
    server written from Scratch, a web server in Swift, a pattern
    matching based library in js, a heuristics based puzzle solver, and
    a web editor for jekyll!  Holy cow!  These presentations are
    extremely inspiring and will probably be the thing I look forward to
    the most, for the next 10 weeks.

-   I can't believe it's already end of week 2. 10 more to go!
