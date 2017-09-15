---
title : "Emacs frame as a pop-up input"
date : "2017-09-14T22:26:00+05:30"
tags : ["emacs", "hack", "life", "writing", "blag"]
draft : false
meta_img : "images/emacs-frame.png"
---

I wanted to try using a dialog box/pop-up window as a prompt to remind me to
periodically make journal entries.  I had the following requirements:

-   Simple, light-weight dialog box that allows text of arbitrary length
-   Ability to launch the dialog from the shell
-   Ability to have some placeholder or template text, each time the dialog is shown
-   Save the input text to a specific `org-mode` file
-   Write as little code of my own, as possible, to do this

I had initially thought about using a tool like `zenity`, or write a simple
dialog box in Python using `Qt`, `wx` or even `tk`, and then yank the input text
at the desired location. This probably wouldn't have turned out to be too hard,
but getting things to look and work exactly the way I wanted would have required
more code than I was willing to write or maintain.

After avoiding doing this for a while, I finally realized that I could simply
use Emacs with a new frame with the appropriate dimensions, and with the correct
file/buffer open to the desired location. This would

-   eliminate the need for me to write the UI myself
-   eliminate the need to do text manipulation in code, to yank it at the right
    place, in the right form. By directly opening up the editor at the required
    location, the onus is on me (as a text inputting user) to put it in, the way I
    want it.
-   additionally provide me the comfort of being able to write with the full power
    of Emacs - keybindings and all that jazz.
-   let me leverage `elisp` to do essentially whatever I want with the buffer
    being displayed as the dialog box.

I ended up with a command that looks something like this

```sh
emacsclient -c -n\
            -F '((title . "Title") (left . (+ 550)) (top . (+ 400)) (width . 110) (height . 12))'\
            -e '(pc/open-journal-buffer)'
```

{{<figure src="/images/emacs-frame.png">}}

This worked pretty nicely, except for the fact that with gnome-shell, the pop-up
frame doesn't always appear raised. It often gets hidden in the Emacs windows
group, and the whole idea of the pop-up acting as a reminder goes for a toss!
But, thanks to [this Ask Ubuntu post](https://askubuntu.com/a/288483), I could fix this pretty easily.

```sh
emacsclient -c -n\
            -F '((title . "Title") (left . (+ 550)) (top . (+ 400)) (width . 110) (height . 12))'\
            -e '(progn (pc/open-journal-buffer) (raise-frame) (x-focus-frame (selected-frame)))'
```
