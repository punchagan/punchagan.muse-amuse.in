---
title: "Elfeed DB backup hooks"
description: "Quick note on my setup for backing up the Elfeed DB"
date: 2026-01-20T23:13:00+05:30
tags: ["elfeed", "emacs", "git", "blag"]
draft: false
---

I had a bunch of things running on my laptop -- video call with screenshare, my
Windows VM, Firefox with a lot of tabs, etc. And my laptop crashed! I didn't
have the time to dig into what, why and how.

Later in the day, I discovered my Elfeed's DB was gone -- blown away. :( I'm
guessing the crash happened in the middle of `elfeed-db-save`, and the data was
lost.

I've now added some back-up for the DB, since I intend to use Elfeed regularly.

```emacs-lisp
(defvar pc/elfeed-db-save-timer nil
  "Timer for debounced elfeed database saves.")

(defun pc/elfeed-db-save-and-backup ()
  "Save the elfeed database and commit to git."
  (when (and (boundp 'elfeed-db) elfeed-db)
    (elfeed-db-save)
    (let ((default-directory elfeed-db-directory))
      (when (file-exists-p ".git")
        (call-process "git" nil "*elfeed-db-backup*" nil "add" "-A")
        (call-process "git" nil "*elfeed-db-backup*" nil "commit" "-m" "auto-backup")
        (call-process "git" nil "*elfeed-db-backup*" nil "push" "origin" "main")))))

(defun pc/elfeed-db-save-soon ()
  "Schedule a database save after 10 seconds of idle."
  (interactive)
  (when pc/elfeed-db-save-timer
    (cancel-timer pc/elfeed-db-save-timer))
  (setq pc/elfeed-db-save-timer
        (run-with-idle-timer 10 nil #'pc/elfeed-db-save-and-backup)))

;; Save and backup when tags change (elfeed-web usage)
(add-hook 'elfeed-tag-hooks   (lambda (&rest _) (pc/elfeed-db-save-soon)))
(add-hook 'elfeed-untag-hooks (lambda (&rest _) (pc/elfeed-db-save-soon)))

;; Save and backup when new entries are added
(add-hook 'elfeed-db-update-hook #'pc/elfeed-db-save-soon)
```
