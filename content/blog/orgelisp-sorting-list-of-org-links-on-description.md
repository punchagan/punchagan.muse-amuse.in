+++
title = "org/elisp - sorting list of org-links on description"
date = "2010-08-20T00:00:00+05:30"
tags = ["code", "emacs", "note", "orgmode"]
draft = false
+++

A small utility function that I used to sort the names of people
who commented on my blog.

```emacs-lisp
(defun org-get-link-desc-from-list ()
  """ Get link description of a list item containing just links """
  (let* ((item-beg (point))
       (item-end (org-end-of-item))
       (cur-item (buffer-substring-no-properties
                  item-beg item-end)))
    (goto-char item-beg)
    (org-columns-compact-links cur-item)))
```

`sort-lines` wasn't good enough for me, since it was sorting
alphabetically and it ended up being the sorted order of the urls
and not the names. This function, when used with
`org-sort-entries-or-items` gave me what I wanted.

Thanks to benny (on #org-mode), I also learnt the difference
between `let` and `let*`.
