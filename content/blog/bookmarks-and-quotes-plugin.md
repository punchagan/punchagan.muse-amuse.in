+++
title = "Bookmarks and Quotes plugin"
date = "2013-10-19T00:00:00+05:30"
tags = ["blog", "code", "nikola", "orgmode"]
draft = false
+++

I used to have a separate page for bookmarks and quotes on the old
blog.  They will now be shared as regular posts with 5 or more
bookmarks/quotes.  I use a bookmarklet in my browser to capture links
to an org-file using org-capture protocol and then I have a small
plugin to Nikola, that looks at such captured bookmarks and quotes and
makes new posts out of them.  This workflow is inspired by Brett
Trepestra's [web excursions](http://brettterpstra.com/2013/01/15/a-web-excursions-system-for-static-blogs/) plugin.

The plugin is currently a part of my blog source, and not published to
Nikola's plugin repository since it is very specific to my setup.  But
if anybody is interested, I can publish the code somewhere public.

If you are interested to get these links and bookmarks into your feed reader,
you can subscribe to their feed: [quotes], [bookmarks](https://punchagan.muse-amuse.in/tags/cat_bookmarks.xml).  These posts will also
make it to the main feed, though.

**UPDATE <span class="timestamp-wrapper"><span class="timestamp">[2015-11-15 Sun 20:45]</span></span>**

-   The quotes feed no longer exists!
-   The bookmarks feed doesn't really get too many updates. I use pinboard for my
    bookmarks, now.
