---
title : "Playing music using mpsyt from Emacs"
date : "2015-04-20T00:00:00+05:30"
tags : ["blag", "emacs", "mpsyt", "python"]
draft : false
---

I've started using the wonderful [mpsyt](https://github.com/np1/mps-youtube/) to play any music from youtube, since
I'm not really interested in the video.  But, since I use emacs for chat/IRC, I
end up getting youtube links into emacs and opening them opens them up in my
browser. I ended up writing some `elisp` to play the songs from within an
instance of `mpsyt` running inside an emacs buffer.

```emacs-lisp
(defun pc/short-url-at-point ()
  "Gets the short url at point.

This function is required only because
`thing-at-point-url-at-point' ignores urls (without a scheme)
that don't start with www."
  (let ((bounds (thing-at-point-bounds-of-url-at-point t)))
    (when (and bounds (< (car bounds) (cdr bounds)))
      (buffer-substring-no-properties (car bounds) (cdr bounds)))))

(defun pc/mpsyt-url (url)
  (let ((buffer (current-buffer))
        (mpsyt-proc-name "*mpsyt*"))

    ;; Start a new term with *mpsyt* if there isn't one
    (unless (get-process mpsyt-proc-name)
      (when (get-buffer mpsyt-proc-name)
        (kill-buffer (get-buffer mpsyt-proc-name)))
      (ansi-term "mpsyt" "mpsyt"))

    ;; Play given url in mpsyt
    (let ((mpsyt-proc (get-process mpsyt-proc-name)))
      ;; If something is already playing, stop it and play this...
      (term-send-string mpsyt-proc "\n\n\n")
      ;; We wait for a bit, since looking for the prompt seems to fail, sometimes?
      (sleep-for 1)
      (term-send-string mpsyt-proc "\n")

      ;; Actually send the command to playurl
      (term-simple-send (get-process mpsyt-proc-name)
                        (format "playurl %s" url)))

    (switch-to-buffer buffer)))

(defun pc/mpsyt-url-at-point ()
  "Play the URL at point using mpsyt."
  (interactive)
  (let ((url (or (url-get-url-at-point) (pc/short-url-at-point))))
    (if (not url)
      (message "No URL found")
        (message (format "Playing %s with mpsyt" url))
      (pc/mpsyt-url url))))

```

The current version of mpsyt crashes when run from inside emacs due to a bug in
the code to get the terminal size, which should be fixed once this [patch](https://github.com/np1/mps-youtube/pull/247) is
merged.

I would've expected `thing-at-point-url-at-point` to be able to find urls even
when they don't have a schema, but it tries to guess the schema from urls and
fails to work when the url starts with `youtube.com` instead of
`www.youtube.com`.

I started off using the command-line interface of `mpsyt` by running it using
`shell-command` or `start-process`.  But, it seemed useful to have a buffer of
`mpsyt` to switch to -- easier to search for new music, repeating songs, etc.
Not all tasks/actions are achievable through `mpsyt`'s command line args.

I ended up writing more code than I thought I would have to[1].  But, I'm
pretty happy with how this all works, right now.

[1] - Isn't it true, more often than not?
