---
title: "A smarter 404 page"
date: 2013-11-11T12:36:53+05:30
tags: ["code", "fuzzy-search", "hack", "js"]
draft: false
---

[Voodoo](http://twitter.com/avudem) found a broken link referring to a one of my posts, on Quora.
Given that I have changed my site generator a bunch of times now, it
is quite possible that there are other broken links at various other
places.  So, I implemented a smart [404 page](https://punchagan.muse-amuse.in/hack) for the site, yesterday.
It is very similar to something I came across on [brettterpstra](http://brettterpstra.com/2013/04/07/fun-with-intelligent-404-pages/)'s site.
I just hooked up [fuse.js](http://kiro.me/projects/fuse.html) with Nikola's [tipue-search plugin](http://getnikola.com/handbook.html#local-search)'s output
file.  My glue code essentially, just figures out the search term from
the URL, performs a Fuse search on the json data created by Nikola's
search plugin, and returns a list of top 5 results.  It just took me
about an hour to write, but is pretty useful, I think.

[(View source of the 404 page)](https://punchagan.muse-amuse.in/hack)
