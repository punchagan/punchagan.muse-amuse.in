---
title : "Blogging with Nikola and Org-mode"
date : "2013-10-16T00:00:00+05:30"
tags : ["blog", "hack", "orgmode"]
draft : false
---

Sigh! I made yet another change to the way this blog gets published.
But, I have a feeling this mechanism, is here to stay!

We've been using Nikola quite regularly for our [Ultimate site](http://ultimatesport.in), and I
quite like it.  I've also contributed a bunch of features to Nikola to
get it to work the way I would like it to.  This weekend I ported my
blog from [o-blog](https://github.com/renard/o-blog) to [Nikola](http://getnikola.com).  The only thing that was stopping me
from doing it, until now is the fact that all my posts are in
org markup and porting them over to one of the formats that Nikola
supports would be a PITA.  So, I wrote a [pretty simple plugin](http://plugins.getnikola.com/#orgmode) to
Nikola to support posting from org files.  And then with a [little
Python](https://gist.github.com/punchagan/6970578), I was able to move everything over to use Nikola.

Hopefully, I'll keep my blog more updated, from here on!
