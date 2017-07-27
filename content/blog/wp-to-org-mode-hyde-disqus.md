+++
title = "WP to org-mode + hyde + disqus"
date = "2010-10-22T00:00:00+05:30"
tags = ["orgmode", "wordpress"]
draft = false
+++

Hello World!

My first post at my new home.  Obviously, it was going to be about the
move.  You knew it, didn't you? ;)

Well, I got some space on the web, along with a few friends.  Thanks to
my org-mode fanboyism, I now use it to maintain my homepage.  I've
successfully completed import of my Wordpress posts and comments. :)


## I now use {#i-now-use}

-   Emacs and Org-mode [^fn:1] to write my posts.
-   `org-hyde.el` [^fn:2] to publish `html` in a `hyde`
    parse-able format.
-   `hyde` [^fn:3] to convert the `html` pages into a blog.
-   `org-publish` to publish other pages in my home page.
-   `git` [^fn:4] and a `bash` script for publishing.
-   Disqus [^fn:5] for the comment system.

Yes, I know it sounds rather complicated. :) But, now that I
have it set up, it's not all that difficult to make a post.
It's just a matter of one `git commit` and `push`.  I need to
fine-tune the shell script a bit, though.


## How I moved {#how-i-moved}

The move definitely wasn't trivial.  I guess, I could've started
afresh but, what fun would that have been? ;)

This roughly how I did things -- in the order that I did them.


### Choosing `hyde` {#choosing-hyde}

I looked at a handful of options to maintain a blog, using
org-mode --- `blorg`, `org-jekyll`, `blorgit`, `ikiwiki`.
After some assessment, I decided upon `org-jekyll` and
`jekyll`.  But then, I accidentally stumbled upon `hyde`.

I decided to go with `hyde` instead of `jekyll` [^fn:6]
since

1.  It's in Python.  I didn't want to start figuring out Ruby,
    now.
2.  It uses Django templates [^fn:7].  And Django is
    something, I wish to learn.  I've started with that. :)


### Clean up `org-jekyll` to work with `hyde`. {#clean-up-org-jekyll-to-work-with-hyde-dot}

I then "ported" `org-jekyll.el` into `org-hyde.el`.

-   removed stuff like categories and languages, that I was not
    going to use.
-   Added some code w.r.t timestamps, from org2blog, to it, so
    that my older `org2blog` posts could be easily ported.


### Clean up older org2blog posts {#clean-up-older-org2blog-posts}

`org2blog` can post either buffers or subtrees.  I had posts in
both formats.  I converted all of them into subtrees of one
tree, using some Python.


### Import older posts {#import-older-posts}

This was the most painful posts.  Importing all the old posts
from Wordpress.  `org-mode` really needs a XHTML/XML importer!

I did all sorts of crazy stuff to get this done.

-   used pandoc to convert html to `markdown`
-   wrote some throw away regex code to convert `markdown` to
    `org-mode`.
-   wrote more regex code to convert `html` to `org-mode`.
-   hacked up a lot of stuff and finally got all the posts into
    `org` format! :)


### A workflow for publishing {#a-workflow-for-publishing}

Set up `git` along with some `bash` code, to have a mechanism
to minimize the effort in making a blog post.  All this is
still a lot of work, compared to the ease with which I used to
use `org2blog`.  That's partly due to `ssh` restrictions in my
hostel.


### CSS clean-up {#css-clean-up}

I'm using the same CSS for `org-mode` published files and
`hyde` published files. I had to clean up my `hyde` templates
and the CSS to make both of them look similar.

My first tryst with CSS hasn't been all that bad. :)


### Installing disqus and importing comments {#installing-disqus-and-importing-comments}

Using disqus was one thing, I wasn't sure I wanted to do.  I
would've loved it if comments could be managed with org-mode
too. ;) [^fn:8]

Anyway, I finally decided to go with it, and I'm quite happy
with it. :)

I loved the ease with which comments could be imported.

1.  Import Wordpress comments using the export `xml` file.
2.  Generate a CSV file containing the URL map -- mapping the
    newer urls to the older ones.
3.  Upload the CSV file and tada!


## Conclusion {#conclusion}

I got to learn quite a few things, during all of this.  I also
have some bits of code, that I can share with you, in case you
are interested.  Leave a comment, if you wish. :)

I'm just hoping to reduce the additional steps required in
publishing to ensure it doesn't add to my already erratic
blogging habits.

[^fn:1]: Org-mode - Homepage
[^fn:2]: Org-hyde is a _port_ of org-jekyll.el
[^fn:3]: Hyde - Github
[^fn:4]: Git - Homepage
[^fn:5]: Disqus - Homepage
[^fn:6]: Github - Jekyll
[^fn:7]: Documentation - Django Templates
[^fn:8]: I feel it is capable of doing that.  It's just my
incapability that prevented me from trying it out.
