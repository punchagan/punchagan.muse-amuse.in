---
title : "Say Howdy with Emacs!"
date : "2015-05-28T00:00:00+05:30"
tags : ["blag", "code", "emacs", "hack", "howdy"]
draft : false
---

Staying in touch with people is something I'm not very good at.  Since I am not
on popular (among my friends/family) networks -- FB and Whatsapp -- I don't
even see random updates from people, to get some sense of being in touch.

I recently read some old posts by Sacha Chua and was inspired by how much code
she had for [contact management](http://sachachua.com/blog/category/geek/emacs/bbdb/) in her old blog posts.  I was inspired by [this
post](http://sachachua.com/blog/2005/05/keeping-in-touch/) in particular to try and be more meticulous about how I stay in touch with
people. Michael Fogleman [blogged](https://mwfogleman.github.io/posts/08-01-2015-emacs-can-keep-in-touch.html) about his contact management work-flow using
`keepintouch`. It seemed to do most of what I wanted, but I wanted this to be
integrated with my `org-contacts-db` and I felt having native elisp code would
make it easier to hook up email, chat, etc. to this.

I ended up writing a small utility called [howdy](https://github.com/punchagan/howdy/) to help me keep in touch with
people. It currently has only a couple of features:

-   <kbd>M-x howdy</kbd> lets me update the last contacted timestamp for a contact.
-   Shows me contacts that I'm out of touch in the agenda, once I add the
    following snippet to an agenda file.

    ```org
    ​* Howdy
      %%(howdy-howdy)
    ```

I also have a few hooks to hook up jabber messages and email to update the db.
I've added them to `howdy-hooks.el` in case anybody else wants to use them.
They can also be used as examples to write other hooks. Feel free to contribute
other hooks or suggest improvements.  The library also ships with a modest test
suite, that will hopefully make it easier for others to contribute.

I'm looking forward to experimenting with this over the next few weeks and
improving it. Hopefully, it'll help me keep in touch, better than I do now.
