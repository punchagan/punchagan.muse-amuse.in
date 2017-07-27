+++
title = "Advice - Programming in Elisp"
date = "2010-08-06T00:00:00+05:30"
tags = ["advice", "emacs", "note", "programming"]
draft = false
+++

Below is a mail sent by Eric Schulte to the org-mode mailing list
answering a query on how to write elisp for org-mode. I am
reproducing it here, since it is useful advice for me. The actual
thread is [here](http://permalink.gmane.org/gmane.emacs.orgmode/27579).

---

The way that I learned how to program in emacs lisp was mainly
using two commands \`elisp-index-search' bound to \`C-h e' on my
system, and most importantly \`describe-function' bound to \`C-h f'.
With \`describe-function' you can look at the source code of
functions whose behavior you are familiar with, you can then copy
portions of the code to your **scratch** buffer where they can be
edited and evaluated with \`eval-defun' bound to \`C-M-x'.  Now with
Babel, instead of doing this in the scratch buffer you could do
this in emacs-lisp code blocks in an org file, enabling notes and
hierarchical organization -- it can be nice to have your noodling
all collected in one file for later reference.

If you are going to do any serious work with lisp, I would
emphatically recommend using paredit-mode, and becoming friends
with the Sexp movement functions

C-M-f	runs the command paredit-forward
C-M-b	runs the command paredit-backward
C-M-u	runs the command backward-up-list
C-M-k	runs the command kill-sexp
C-y	runs the command yank

They allow you to manipulate lisp code on the level of logical
expressions, the utility of which can not be over stated.

As for working with Org-mode in particular, I'd recommend looking
at the documentation and source-code of Org-mode functions with
\`describe-function', and then looking for how these functions are
actually used in the Org-mode code base with \`rgrep'.

For a more structured learning experience, I've heard very good
things about <http://www.gnu.org/software/emacs/emacs-lisp-intro/>,
although I haven't used it myself.

Hope this helps.  Happy Hacking -- Eric

---
