---
title : "org-drill for making it stick!"
date : "2015-01-17T00:00:00+05:30"
tags : ["blag", "emacs", "hack", "hackerschool", "learning", "orgmode"]
draft : false
---

Those who read the [last](https://punchagan.muse-amuse.in/posts/learning-to-use-org-drill.html) [few](https://punchagan.muse-amuse.in/posts/learning-about-spaced-repetition-supermemo-org-drill-et-al.html) [posts](https://punchagan.muse-amuse.in/posts/more-input-sources-for-org-drill.html) here, would know that I have been
experimenting with [org-drill](http://orgmode.org/worg/org-contrib/org-drill.html) (a spaced repetition extension to [Org mode](http://orgmode.org/)).  I
have been using the system (almost) religiously for the past 2 months, and I do
find that it has helped a great deal! (in some respects).  I have also spent a
considerable amount of time trying to reduce the friction to put new stuff into
the system, and am constantly on the look out for further improvements.

Using this system has definitely helped with retention, and I find that I can
recall quite a few things I have read a few weeks ago, that I would normally
have been unable to. Though, I can recall a lot of information, I have been
having a feeling of "fragmentation": the feeling of just retaining individual
bits/fragments of information, while losing out on actually internalizing the
knowledge; not seeing the big picture, etc.

Wozniak (the author of super-memo) [warns against](http://www.supermemo.com/articles/20rules.htm) learning without
understanding, and memorizing before actually learning stuff.  I haven't
consciously added stuff into the system that I didn't understand (when I added
it), but, later it does feel like I have lost some connections or the
understanding, and am only holding onto the fragments of information.

The problems as explained in (read: as interpreted by me from) [Make it Stick](http://www.amazon.com/Make-Stick-Science-Successful-Learning/dp/0674729013/ref=sr_1_1/188-6768042-2821103?ie=UTF8&qid=1421439099&sr=8-1&keywords=make+it+stick&pebp=1421439103302&peasin=674729013)
appear to be:

1.  The understanding (if any) at the time of adding stuff into the
    spaced-repetition system is untested.  It may just be familiarity
    masquerading as understanding.

2.  The lack of any spaced repetitions for the overall concept/understanding and
    actual repetitions only for individual bits doesn't help retention of the
    understanding (even if there was any, in the first place).

To work around this, I'm going to try adding questions that test understanding,
to the system.  The Super-memo team strongly recommends keeping the drill items
small and easy to answer.  This may be helpful in keeping each drill session
short, but I would really like to add conceptual questions to the system, and
see how it goes. I hacked `org-drill` to allow me to type out answers, before
looking at the "correct" ones.  This is an adaptation of a system that a fellow
Hacker Schooler uses, and shared.  Also, hopefully forcing myself to type out
the answer will help me get around the problem of sometimes saying "yeah I know
that", then looking at the answer only to reaffirm the feeling of familiarity,
rather than actually testing myself.  I'm still going to continue adding quick
and short questions that test "bits of information", though. But, hopefully the
additional conceptual questions are going to tie things together and help fill
in the gaps.  Lets see how this goes!

For those interested, my hacks to `org-drill` below.  The code is really a
hack, and welcome any suggestions on cleaning up the code.

```emacs-lisp
(advice-add 'org-drill-presentation-prompt :around 'pc/org-drill-presentation-prompt)

(defun pc/org-drill-presentation-prompt (old-fun &rest fmt-and-args)
  "A presentation prompt that allows capturing answers."

  (let ((cb (current-buffer))
        (heading (nth 4 (org-heading-components)))
        (entry-id (org-entry-get (point) "ID"))
        (input ""))
    (switch-to-buffer-other-window "*org-capture-drill-answer*")
    (org-mode)
    (insert "# Hit C-c C-c once you are done answering!\n")
    (org-insert-heading-respect-content)
    (insert (format "Answer: %s" heading))
    (org-entry-put (point) "QUESTION_ID" entry-id)
    (goto-char (point-max))
    (insert "  ")
    (org-time-stamp-inactive '(16))
    (insert "\n\n  ")
    (while (not (and input (equal input "")))
      (ignore-errors
        (execute-kbd-macro input))
      (setq input (read-key-sequence nil)))
    (switch-to-buffer-other-window cb)
    (apply old-fun fmt-and-args)))

(advice-add 'org-drill-reschedule :around 'pc/org-drill-reschedule)

(defun pc/org-drill-reschedule (old-fun)
  "Calls the original reschedule, but also archives the answer"
  (prog1 (funcall old-fun)
    (let ((cb (current-buffer)))
      (switch-to-buffer-other-window "*org-capture-drill-answer*")
      (pc/org-refile-to-datetree "drill.org_archive")
      (message (buffer-name))
      (switch-to-buffer-other-window cb)
      (kill-buffer "*org-capture-drill-answer*"))))

(require 'org-datetree)
(defun pc/org-refile-to-datetree (journal)
  "Refile an entry to journal file's date-tree"
  (interactive "fRefile to: ")
  (let* ((journal (expand-file-name journal org-directory))
         (date-string (or (org-entry-get (point) "TIMESTAMP_IA")
                          (org-entry-get (point) "TIMESTAMP")))
         (dct (decode-time (or (and date-string (org-time-string-to-time date-string))
                               (current-time))))
         (date (list (nth 4 dct) (nth 3 dct) (nth 5 dct))))
    (org-cut-subtree)
    (with-current-buffer (or (find-buffer-visiting journal)
                             (find-file-noselect journal))
      (org-mode)
      (save-excursion
        (org-datetree-file-entry-under (current-kill 0) date)
        (bookmark-set "org-refile-last-stored")))
    (message "Refiled to %s" journal)))
```
