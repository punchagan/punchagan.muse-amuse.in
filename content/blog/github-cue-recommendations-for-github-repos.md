---
title : "GitHub Cue: Recommendations for GitHub Repos"
date : "2011-08-05T00:00:00+05:30"
tags : ["app", "chrome", "code", "github", "hack"]
draft : false
---

If you aren't already aware of it, I'm one of those people who
goes around saying, "GitHub is my Facebook".  I spend quite a lot
of time on GitHub, browsing the work of various people, looking at
loads of interesting stuff that people built.  I keep jumping
between people pages and projects using the Watchers/Watching &
Followers/Following pages.  This way, I do come across interesting
people and projects, but the SNR is too low.  I wanted a better
way to be able to see stuff, that I find interesting.  That's how
the idea for this Chromium app -- GitHub Cue -- was born.

@baali and I hacked on this, during the last few days and got it
working.  It works as follows, (from the README) ---

1.  Scrapes all the descriptions of the repositories being watched
    by the user.
2.  Key terms are extracted from this description text using the
    Yahoo Term Extractor.
3.  A list of languages is obtained, based on the languages of the
    repositories, the user if watching.
4.  GitHub searches are performed for a combination of 3 randomly
    chosen languages and 5 random key terms.
5.  10 random repositories out of all these, are shown.

This is a very simplistic algorithm, but works decently for my
purposes.  Ideally, I would've liked to use a Collaborative
Filtering algorithm, but I found the data to be too sparse, and
the amount of computation to be too much to be done on the fly.  I
wasn't really interested in pre-computing stuff and putting it
onto my server.  I settled down to the next best thing I could
think of.

I would appreciate any further ideas and suggestions.  Thanks!
