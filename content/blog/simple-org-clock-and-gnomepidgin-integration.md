---
title : "Simple org-clock and gnome/pidgin integration"
date : 2014-10-22T16:43:35-04:00
tags : ["code", "emacs", "orgmode"]
draft : false
---

**See update [below](#orge999abb)**

I have been trying to get back to using org-mode and its clocking
functionality, more often than not.  I used to use it a lot, a few years ago,
and haven't been using it, since I had been in my last job.

To help with it, I decided to integrate clocking in and out with changing
status on Pidgin, and turning notifications on and off in Gnome.  Here's a few
lines of code that does this for me.

```emacs-lisp

(defadvice org-clock-in (after pc/org-clock-in (&optional select start-time))
  "Turn gnome notifications off."
  (dbus-send-signal
   :session
   "org.gnome.SessionManager"
   "/org/gnome/SessionManager/Presence"
   "org.gnome.SessionManager.Presence"
   "SetStatus" 2)
  (shell-command "purple-remote setstatus?status=unavailable"))

(defadvice org-clock-out (after pc/org-clock-out (&optional switch-to-state fail-quietly at-time))
  "Turn gnome notifications back on."
  (dbus-send-signal
   :session
   "org.gnome.SessionManager"
   "/org/gnome/SessionManager/Presence"
   "org.gnome.SessionManager.Presence"
   "SetStatus" 0)
  (shell-command "purple-remote setstatus?status=available"))

```


## Update <span class="timestamp-wrapper"><span class="timestamp">&lt;2014-11-01 Sat&gt;</span></span> {#update-span-class-timestamp-wrapper-span-class-timestamp-and-lt-2014-11-01-sat-and-gt-span-span}

[@baali](http://baali.muse-amuse.in) tried to use my code, and it turns out it didn't work for him, because I
forgot to mention that `(ad-activate 'org-clock-in)` needs to be run, after the
`defadvice` code.  I have no idea how it worked for me, without doing that.
May be because I have `defadvice` for other functions?

Also, while debugging this, I found that `defadvice` is a deprecated way of
doing this, and `add-function` is the way to go now.  But, instead of advising
the function, I decided to make use of `org-clock-in-hook`.

Here is the new code.

```emacs-lisp
(defun pc/turn-off-notifications ()
  "Turn gnome notifications off."
  (dbus-send-signal
   :session
   "org.gnome.SessionManager"
   "/org/gnome/SessionManager/Presence"
   "org.gnome.SessionManager.Presence"
   "SetStatus" 2)
  (shell-command "purple-remote setstatus?status=unavailable"))

(defun pc/turn-on-notifications ()
  "Turn gnome notifications back on."
  (dbus-send-signal
   :session
   "org.gnome.SessionManager"
   "/org/gnome/SessionManager/Presence"
   "org.gnome.SessionManager.Presence"
   "SetStatus" 0)
  (shell-command "purple-remote setstatus?status=available"))

(add-hook 'org-clock-in-hook 'pc/turn-off-notifications)
(add-hook 'org-clock-out-hook 'pc/turn-on-notifications)
```
