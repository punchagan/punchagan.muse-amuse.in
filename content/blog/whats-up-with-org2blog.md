---
title : "What's up with org2blog?"
date : "2011-01-15T00:00:00+05:30"
tags : ["org2blog", "wordpress"]
draft : false
---

Another post on `org2blog`.  Yes, the project is still alive. ;)
Well, frankly quite a few people seem to be using it, and I
regularly get bug-reports and feature requests.  I'm happy. :)

Actually, this post is to announce a change in the namespace of
**my** org2blog.  It turns out that there is another package that is
called org2blog, but it posts to blogger.  Tehom, the author of
the other package got in touch with me, and we tried to clean up a
few things.  In this process, we decided to use two different
namespaces, to avoid conflicts if a particular user has both the
packages loaded.  I am going to use `org2blog/wp` as my namespace
prefix, instead of the older `org2blog`.  So, if you are posting a
sub-tree, you'll need to use the `org2blog/wp-post-subtree`
function, instead of `org2blog-post-subtree`.

We, Tehom and I, did discuss the possibility of merging the two
packages into a single huge package, but we think the amount of
work is far greater than the payoffs.  So, the packages continue
to be called `org2blog` but we reference each others packages, to
reduce the confusion, amongst users.

`org2blog/wp` version 0.4 comes with the new namespace.
