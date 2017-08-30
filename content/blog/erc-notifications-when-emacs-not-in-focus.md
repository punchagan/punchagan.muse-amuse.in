---
title : "erc-notifications when Emacs not in focus"
date : "2014-11-06T00:00:00+05:30"
tags : ["emacs", "hack"]
draft : false
---

I have been trying to get ERC working with notifications. Julien Danjou's
wonderful [notifications](https://julien.danjou.info/blog/2012/erc-notifications) module for ERC is great, but it is annoying to get
notifications even when Emacs is in focus.

I had looked at [circe-notifications](https://github.com/eqyiel/circe-notifications/blob/master/circe-notifications.el), which has the feature but uses xdotool and
xprop to do it.  I was looking for something simpler, though... and it suddenly
struck me that I have an auto-save hook in Emacs that is run when I focus out
of it.  I wondered if I could disable and enable notifications on focus, and it
worked.

In case it is useful for somebody else -

```emacs-lisp
(add-to-list 'erc-modules 'notifications)
(erc-notifications-mode)
(add-hook 'focus-out-hook 'erc-notifications-enable)
(add-hook 'focus-in-hook 'erc-notifications-disable)
```

I wonder if there are some corner cases where this doesn't work, and that's why
the author of circe-notifications chose the tools that he did.
