---
title: "Goodbye Google Analytics"
date: 2018-11-06T21:47:00+05:30
tags: ["blog", "blag", "rust", "philosophy", "statistics"]
draft: false
---

TL; DR: My blog no longer has Google Analytics. And I'm happy about it.


## Why I had it? {#why-i-had-it}

I've been using Google Analytics for many years now - ever since I moved to a
static blog, from WordPress. WordPress had [built-in analytics](https://en.support.wordpress.com/stats/), and it seemed
natural to me to have analytics on the static site too, after using WP for a
couple of years or so.

I checked the analytics only once in a while, But, I did find it encouraging and
sometimes amusing to see where and how people ended up on my blog. Especially
so, when a post became popular.


## Why I removed it? {#why-i-removed-it}

A few months ago, around the time when we were all [bombarded by GDPR related
policy change announcements](https://en.wikipedia.org/wiki/General%5FData%5FProtection%5FRegulation#Timeline) from random services we signed up to and forgot
about, I decided to remove Google Analytics on my blog.

I also received an email from Google Analytics, listing a bunch of changes I'd
need to make to how I use anlaytics, to be GDPR compliant. That made me
reconsider if it was worth having analytics on my site.

I use [Ghostery](https://www.ghostery.com/) and other such tools to minimize how much people are able to
track me. It feels better to not have the same kind of analytics that I'm averse
to, on my blog.

Also, about half the people who read my blog likely don't like analytics, and
are [probably blocking](http://blog.wesleyac.com/posts/google-analytics) it. Considering how little I used the analytics, I just
didn't see a point in keeping it running.


## But what about the useful stats? {#but-what-about-the-useful-stats}

My blog doesn't get too many visits -- only a few dozen people every week --
mostly my friends or acquaintances. There's not as much going on, to find
anything super interesting in the stats.

Nevertheless, it is sometimes interesting to see where people end-up coming to
my blog from. And [on one occasion](https://punchagan.muse-amuse.in/blog/a-smarter-404-page/), I found a broken link to a blog post of mine
which was sending a significant number of people to my blog. I fixed that, and
also added a 404 page with helpful suggestions.

I have the proxy of interactions on twitter or texts/emails from friends, to
gauge how interesting a post was. But, it's useful to have some kind of
analytics to gauge the interest and reading patterns of older posts.

Given this, and the fact that I've recently been intrigued by [Rust](https://www.rust-lang.org/en-US/) and want to
learn it, I've started writing a [small Apache log analyzer in Rust](https://github.com/punchagan/weblogviz). It's just a
toy, as of now. [goaccess](https://goaccess.io/) is a nice "real-time" log analyzer that gives some nice
stats, if you are looking for a nicer tool.

---

Thanks [Shantanu Choudhary](<http://baali.muse-amuse.in/>) for prompting me to
write this post, reading a draft of this, and giving helpful suggestions to make
it better.
