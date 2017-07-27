+++
title = "A couple of counting functions"
date = "2010-09-17T00:00:00+05:30"
tags = ["code", "emacs"]
draft = false
+++

I had a strict character limit of 180 chars for something I was
writing. I just wrote a simple function to count characters in a
region or a buffer. Another function to count the words.

```emacs-lisp
(defun count-chars ()
  "Count the number of chars in a buffer or region."
  (interactive)
  (let* ((beg (if (region-active-p) (region-beginning) (point-min)))
         (end (if (region-active-p) (region-end) (point-max))))
         (message (number-to-string (- end beg)))))
```

```emacs-lisp
(defun count-words ()
  "Count the number of words in a buffer or region."
  (interactive)
  (let* ((beg (if (region-active-p) (region-beginning) (point-min)))
         (end (if (region-active-p) (region-end) (point-max)))
         (count 0))
    (save-excursion
      (goto-char beg)
      (while (< (point) end)
        (forward-word)
        (setq count (1+ count))))
    (message (int-to-string count))))
```
