---
title : "Error messages and new users"
date : "2016-05-17T00:00:00+05:30"
tags : ["blab", "programming", "software", "user-experience"]
draft : false
---

I was helping a friend of mine setup [his blog](http://jajoosam.github.io) and we were trying to use [Hexo](http://hexo.io) --
a static site generator.  We chose a Javascript based tool since he's trying to
learn Javascript.  I skimmed through active Javascript projects in [this list](https://staticsitegenerators.net)
and finally zeroed down upon Hexo based on its popularity.  I promised to help
my friend to set this up, but he first tried to do it on his own and got back
to me after an hour or so, quite frustrated and almost on the verge of giving
up setting it up.  I didn't expect this from a tool that had so many stars,
forks, plugins and so much active development.

We finally got it working, but we found that the error messages were horrendous
-- even for someone who has been using free and open-source tools for a while
now.  Printing out errors from compiler or interpreter directly along with the
stack trace is almost always the worst thing to do for a tool/utility (as
opposed to an API or library).  The stack trace is definitely useful, for
developers trying to build upon or improve your tool.  Have a debug or
development mode where developers can get all the information they need.

If you care about your users, especially new users, make sure you spend
sufficient time on showing human-readable messages. If possible list the
possible causes for every error along with tips for troubleshooting.
