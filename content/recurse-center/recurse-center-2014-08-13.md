+++
title = "Recurse Center, 2014-08-13"
date = 2014-08-14T11:11:59-04:00
tags = ["python"]
categories = ["recursecenter"]
draft = false
+++

-   I feel like I didn't get much done yesterday.
-   I mostly worked on the API differ, but didn't get much done.  I have a few
    tests, and some code for diffing two functions, but I'm not very happy with
    it.
-   I helped Giorgio and Carlos with using my client only `hs_oauth`
    script/library, for their Zulip bot.
-   The white boarding group worked on some binary related problems, and it was
    fun.
-   I looked at how the HS OAuth backend works on blaggregator and thought about
    how to go about fixing the issue of broken images on the site.  The problem
    happens because the image URLs are returned from the HS API calls, that are
    made whenever a user logs in(?), and the URLs are cached.  Since, HS uses
    cloudfront for its assets, the URLs expire after a period of time, and the
    cached urls in blag's database need to be updated.  There could be two ways
    of doing it -

    1.  Check if the URL 404s, every time a URL is requested, on the server side.
    2.  Do it on the client side, with some javascript magic.

    Intuitively, I feel like 2. would be better, but Madhu suggested
    that 1. wouldn't be that bad either.  We could try both out, and see which
    works better I suppose.

    I'd be interested to try this out, sometime.
