---
title : "Refile to date-tree"
date : "2010-07-30T00:00:00+05:30"
tags : ["code", "emacs", "orgmode"]
draft : false
---

Useful to refile notes to the journal file, which is a
date-tree. `org-refile` isn't convenient to refile stuff to a
date-tree.

```emacs-lisp
(defun my/org-refile-to-journal ()
  "Refile an entry to journal file's date-tree"
  (interactive)
  (require 'org-datetree)
  (let ((journal (expand-file-name "journal.org" org-directory))
        post-date)
    (setq post-date (or (org-entry-get (point) "TIMESTAMP_IA")
                        (org-entry-get (point) "TIMESTAMP")))
    (setq post-date (nthcdr 3 (parse-time-string post-date)))
    (setq post-date (list (cadr post-date)
                          (car post-date)
                          (caddr post-date)))
    (org-cut-subtree)
    (with-current-buffer (or (find-buffer-visiting journal)
                             (find-file-noselect journal))
      (save-excursion
        (org-datetree-file-entry-under (current-kill 0) post-date)
        (bookmark-set "org-refile-last-stored")))
    (message "Refiled to %s" journal))
  (setq this-command 'my/org-refile-to-journal))

(defun my/org-agenda-refile-to-journal ()
  "Refile the item at point to journal."
  (interactive)
  (let* ((marker (or (org-get-at-bol 'org-hd-marker)
                     (org-agenda-error)))
         (buffer (marker-buffer marker))
         (pos (marker-position marker)))
    (with-current-buffer buffer
      (save-excursion
        (save-restriction
          (widen)
          (goto-char marker)
          (org-remove-subtree-entries-from-agenda)
          (my/org-refile-to-journal)))))
  (org-agenda-redo))

(org-defkey org-agenda-mode-map (kbd "C-c C-S-w") 'my/org-agenda-refile-to-journal)
(org-defkey org-mode-map (kbd "C-c C-S-w") 'my/org-refile-to-journal)
```

Enjoy!

**Update <span class="timestamp-wrapper"><span class="timestamp">[2016-06-16 Thu]</span></span>** [Raam Dev](https://twitter.com/raamdev) pointed me to an [issue](http://emacs.stackexchange.com/questions/21322/preventing-org-cut-subtree-from-appending-subsequent-cuts-to-previous-kill-ring) and a suggested fix, that
 I have updated the above code with.
