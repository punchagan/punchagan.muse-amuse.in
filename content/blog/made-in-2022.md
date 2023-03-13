---
title: "Made in 2022"
date: 2023-03-08T23:35:00+05:30
tags: ["blag", "software", "tools", "hack"]
draft: false
---

Keeping with last year's tradition, this post comes when we are almost 1/5th
through this year.


## 2022 projects {#2022-projects}

[Expense Tracker](https://github.com/punchagan/expense-tracker)
: I built a personal Expense Tracker over the month of
    October using SQLite and Streamlit, because I wasn't comfortable sharing my
    financial data with a 3rd party. I've tried to keep it simple, so it's not a
    pain to use.  But, I've also tried to keep it extensible, for others to try
    and use.

    The last few months have been quite busy personally, and I haven't been able
    to use it as much as I would like to, but hopefully things will settle down
    soon.  A couple of things that I'd like to improve:

    -   The Sqlite file is stored locally, and the data is not synced between
        different computers.

    -   The tagging/categorization of expenses is very manual, and a little bit
        more automation would be handy.


[artful-dodger](https://github.com/punchagan/artful-dodger/)
: A Next.js project for hosting an art/photo gallery with
    metadata stored in a Google Spreadsheet and images in a Google Drive (with an
    optional CDN, recommended). I built this for a friend, who is experimenting
    with creating "a more equitable model for curating, buying, and selling
    art". The gallery is currently in "private beta", and I can't link to
    it. But, here's a sample gallery [here](https://punchagan.github.io/artful-dodger/), whose configuration lives [here](https://github.com/punchagan/artful-dodger/blob/main/.env.local.default).


[ox-gist](https://github.com/punchagan/ox-gist)
: I released my first Emacs MELPA package -- [ox-gist](https://melpa.org/#/ox-gist) -- an Orgmode
    backend to export and update sub-trees and buffers to GitHub gists.  It was a
    great experience contributing to MELPA.  I wrote a blog post about it [too](https://punchagan.muse-amuse.in/blog/ox-gist/).


[Termux scripts](https://github.com/punchagan/android-dotfiles/tree/main/bin)
: I've started using Termux on my Android phone and have
    found the Text-to-Speech (TTS) API quite handy.  I've a couple of scripts on
    my phone that lets me use TTS to read out contents on the clipboard or an
    article from my browser.


[Fantasy League Site](https://github.com/india-ultimate/fantasy)
: With help from a bunch of volunteers collecting and
    validating data, [Jonny](https://github.com/Joe2k) and I built a [website](https://fantasy.indiaultimate.org/) for the Fantasy League for
    Indian Ultimate State Championships. There was nothing technically
    challenging about the project, but it just involved a lot of data cleaning
    and co-ordination between the volunteers. The data was collected using pen
    and paper, instead of a digital app for collecting the stats.  This made the
    data cleaning and validation significantly harder. I'd definitely push for
    digital data collection if people try to do something like this again.


[Bookmarklets](https://github.com/punchagan/bookmarklets)
: A [web-page](https://punchagan.github.io/bookmarklets/) with a bunch of Bookmarklets from my browser's
    Bookmarks bar. I've had most of them around for a while, but putting them on
    a web page makes it easy to share and find myself on other
    browsers/computers.


Music
: Unlike 2021, I've only been able to record a couple of songs. And
    this year (2023) hasn't been any better, so far. I hope I'll be able to make
    amends to this, soon, though.


## Review of 2021 projects {#review-of-2021-projects}

[Earworm](https://github.com/punchagan/earworm/)
: I didn't make any updates to the package, not because it's perfect
    but because I didn't use it much in 2022 -- thanks to how little I've been
    able to record.

    While, writing this blog post I realized that workflow had a couple of
    annoyances. I improved the code to fix them.

    1.  I need to move an audio file back-and-forth between my phone and my
        laptop, one full round trip to add ID3 tags and cover image.  This makes
        me put off uploading recorded files to the site.  Also, the new media file
        needs to be named in a specific format.  I've added a new CLI subcommand
        to automate all of this for me.

    2.  I always need the full collection of the music files on the computer,
        where I'm updating the site from. I can just `scp` the existing site onto
        my computer and merge the media directories.


[Ukulele Tutorials Aggregator](https://ukulele.muse-amuse.in/)
: The job of manually updating the site is a
    lot of work, and I haven't had the interest to keep doing it.


RPi Server and Phone Backup
: The physical setup was accidentally dismantled
    by folks I share my physical space with, and I haven't been able to put back
    everything in place, yet.  I'm hoping I'll be able to get back to doing this
    at some point this year.


## Outro {#outro}

I've already built a couple of small things in 2023, and I hope I am able to
find some interesting things to do this year.

Link to the [2021](https://punchagan.muse-amuse.in/blog/made-in-2021/) post.
