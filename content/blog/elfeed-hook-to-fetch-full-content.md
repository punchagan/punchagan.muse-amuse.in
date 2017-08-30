---
title : "Elfeed hook to fetch full content"
date : "2015-12-19T00:00:00+05:30"
tags : ["blag", "elfeed", "emacs", "hack", "pinboard"]
draft : false
---

I have started to use [Pinboard](http://pinboard.in)'s `unread` tag as my to-read list.  It has a
bookmark-let that works pretty well for adding stuff into my "to-read" list.  I
then catch up on this list using `elfeed` and subscribing to the unread items'
RSS feed.  The work-flow is pretty nice for adding stuff into the list, and
finding items on the list. But, when it comes to the actual reading part, the
entries in the feed don't have the actual content I want to read, and I end up
opening the links in a browser.

Inspired by a [comment from FiloSottile](https://github.com/sursh/blaggregator/pull/80#issuecomment-165849126), I realized it should be pretty easy to
setup a hook that fetches the actual content to make my reading work-flow
smoother. I wrote a [small script](https://github.com/punchagan/dot-files/blob/master/bin/get_article.py), using [python-readability](https://github.com/buriy/python-readability), to fetch the page
content, given a URL. This script is then hooked onto `elfeed-new-entry-hook`,
to fetch content of for new entries as they are fetched.  All the old entries
can be easily fixed with a single call to `elfeed-apply-hooks-now`.

```emacs-lisp
(defun pc/get-url-content (url)
  "Fetches the content for a url."
  (shell-command-to-string (format "~/bin/get_article.py %s" url)))

(defun pc/get-entry-content (entry)
  "Fetches content for pinboard entries that are not tweets."
  (interactive
   (let ((entry elfeed-show-entry))
     (list entry)))

  (let ((url (elfeed-entry-link entry))
        (feed-id (elfeed-deref (elfeed-entry-feed-id entry)))
        (content (elfeed-deref (elfeed-entry-content entry))))
    (when (and (s-matches? "feeds.pinboard.in/" feed-id)
               (not (s-matches? "twitter.com/\\|pdf$\\|png$\\|jpg$" url))
               (string-equal "" content))
      (setq content (pc/get-url-content url))
      (setf (elfeed-entry-content entry) (elfeed-ref content)))))

(add-hook 'elfeed-new-entry-hook #'pc/get-entry-content)
```
