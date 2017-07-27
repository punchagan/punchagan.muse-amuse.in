+++
title = "Reading-time based scheduling"
date = "2016-06-06T00:00:00+05:30"
tags = ["blag", "hack", "idea", "programming", "reading"]
draft = false
+++

I had posted a link to an poem written on Medium on a Slack channel that I use
with friends.  A friend said that she liked the fact that the Slack article
preview had the reading time from Medium in it.  She could decide whether or
not she wanted to read the poem or any other article at that moment.

This gave me the idea for a reading time extension for my [browser](https://www.chromium.org/getting-involved/download-chromium), or my [feed
reader](https://github.com/skeeto/elfeed) or my [bookmarks](https://pinboard.in) -- my reading list.  The first version should be able to
compute or extract the reading time for an article or a tab in my browser, and
index them.  I want to be able to specify the amount of time I will be able to
spend reading, and be presented with something from my reading list.  I think
this would help with scheduling the reading of longer articles, and also to
actually help me get through my reading list.

Reading time estimates that use heuristics based on word-count may not really
work, and may do [more harm than good](https://medium.com/@fchimero/this-should-only-take-a-minute-or-four-probably-e38bb7bf2adf#.mvkd09m6m).  But, it may still be worth a try to see
if it helps my reading habits in any way.  A quick search pointed me to [this
extension](https://chrome.google.com/webstore/detail/readism-article-reading-t/bmiolhceebkeljaikojgcoeefblcihje), that can give the reading time for any page but doesn't really do
what I want.
