---
title : "Clock in and get-shit-done"
date : "2015-12-22T00:00:00+05:30"
tags : ["blag", "emacs", "orgmode"]
draft : false
---

I had [setup](./simple-org-clock-and-gnomepidgin-integration.html) a couple of hooks about an year ago that turn off all notifications
while I'm clocking in. But, I find myself switching to the browser and jumping
to twitter, out of habit.  I've tried [get-shit-done](https://github.com/leftnode/get-shit-done) in the past to help myself
break this habit. But enabling get-shit-done manually is step that quickly
became a non-habit.

So, I hooked up get-shit-done into an `org-clock-in-hook`.  The snippet below
is what I added into a function that is added to this hook.

```emacs-lisp
(with-temp-buffer
  (cd "/sudo::/")
  (shell-command "HOME=/home/punchagan get-shit-done work"))
```

`get-shit-done` needs to be run as `root`, since it does things like modifying
`/etc/hosts` and restarting networking.  Just calling `get-shit-done` as a
shell command fails with the error `sudo: no tty present and no askpass program
specified`.  I found a couple of ways to fix this. The snippet above
piggy-backs on tramp to allow for a way to enter the password for `sudo` to
use. This also means that I don't need to enter the password, as long as the
tramp connection is alive.

For someone worried about having such an easy way of running something as
`root`, using something like `gnome-ssh-askpass` as the askpass program might
work better.

```emacs-lisp
(shell-command "SUDO_ASKPASS=\"/usr/lib/openssh/gnome-ssh-askpass\" get-shit-done work")
```
