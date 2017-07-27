+++
title = "Scraping Google Groups"
date = "2013-12-31T00:00:00+05:30"
tags = ["email", "hack", "idea", "mumbai", "ultimate"]
draft = false
+++

I was playing around with a few ideas for creating a timeline for the
mumbai ultimate group, and as a part of playing around with stuff, for
that idea, I ended up wanting to scrape all the emails on our google
group.  After looking around a little bit, I failed to find anything
that claims to be able to do this.

So I ended up writing my own [hacky script](https://gist.github.com/punchagan/7947337) to download all the emails
sent on the group.  Like I said, this is a hack and can be improved
quite a bit, but I am not inclined to do anything about it, right
now.  Since, everything about google groups is ajaxy, this script uses
selenium and does things on the page, that one would do by hand.  It's
not something that I am proud of, but it does the job!
