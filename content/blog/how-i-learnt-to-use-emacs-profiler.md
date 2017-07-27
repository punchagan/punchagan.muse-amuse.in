+++
title = "How I learnt to use Emacs' profiler"
date = "2015-01-03T00:00:00+05:30"
tags = ["emacs", "orgmode", "programming"]
draft = false
+++

I learnt to use Emacs' profiler yesterday, after many hours of yak-shaving,
trying to get [Memacs](https://github.com/novoid/Memacs) working.  Memacs is a [memory extension](http://en.wikipedia.org/wiki/Memex) system for Emacs
written by Karl Voit, that I have been meaning to try out for a long time now.
Seeing lots of review posts at the turn of the year and watching Karl's recent
[Emacs Chat with Sacha Chua](http://emacslife.com/emacs-chats/chat-karl-voit.html) pushed me to try and finally set it up.

I started writing a [module](https://github.com/punchagan/Memacs/blob/chrome/memacs/chromium.py) to create a Memacs file -- an org archive file --
from my browser history.  It was pretty easy to write, and I had it spitting
out a huge file with 22k entries after about a couple of hours of work.  Then I
excitedly pulled up my agenda, and turned on the option to view archived
entries, only to be super-disappointed.  It turned out to be extremely slow!
Actually, the agenda never came up with the 22k entries file that I had. At
least not in 5 or so minutes, before I got impatient.  The performance was
unacceptable even when I reduced it to 5k entries.

I was pretty sure it wasn't that slow for Karl in his [demo](https://www.youtube.com/watch?v=SaKPr4J0K2I#t=999) and [tweeted](https://twitter.com/punchagan/status/550723377871065088) to him,
asking for a workaround. Meanwhile, I looked at his dot-emacs, but wasn't able
to dig out what was needed to speed up things. He confirmed that his
performance was way better than what I was getting.

First, I ruled out the possibility of it being because of the SSD, since
clearly my CPU usage was peaking, and the task was CPU bound and not I/O.
Next, I tried using the same file on a different machine (with a different
version of Emacs and org-mode), and it worked blazingly fast.  So, it was
either the version of Emacs or org-mode that I was using.

I should have stopped, thought clearly, and started experimenting with org
version, but hindsight is 20-20.  I tried Ubuntu's pre-built Emacs and agendas
were fast!  I suspected my Emacs build, since I recently started building Emacs
from git.  I built two or three other versions of Emacs, and wasted a lot of
time, before realizing that I wasn't using the org-mode source bundled inside
Emacs for the tests, and there were two "independent" variables.

Finally, I began bisecting org-mode's source and found that all hell broke
loose with an [inconspicuous change](http://orgmode.org/w/?p=org-mode.git;a=commitdiff;h=b88c5464db2cb0d90d4f30e43b5e08d2b1c1fcea;hp=8cc4e09950594b2abec2502e9218318570595ac5) around release 8.2.6.  It turns out that
org-overview was broken before this, and collapsing all the trees in a newly
opened org-buffer (default option) wasn't working. Once this bug was fixed,
opening huge org files would slow down by a great deal, in turn causing agenda
generation to be unbearably slow.

All I had to do was add a `#+STARTUP: showeverything` to the top of the file.
This speeded up things by about 50 times!  It turns out, I later found out,
that all of this is documented on [Worg](http://orgmode.org/worg/agenda-optimization.html). I did try a few search engine queries,
but sadly none of them brought this up.  Adding the following to my config,
speeded up agenda generation by about 150-200 times!

```emacs-lisp
(setq org-agenda-inhibit-startup t) ;; ~50x speedup
(setq org-agenda-use-tag-inheritance nil) ;; 3-4x speedup
```

In the course of all this debugging, I learnt how to use Emacs' profiler.  The
profile reports along with git bisect, eventually helped me figure out what the
problem was.

To profile the CPU usage, all you have to do is add a call like

```emacs-lisp
(profiler-start 'cpu)  ;; or M-x profiler-start
```

at the place where you wish to start it.  Emacs will then start collecting
information about where time is being spent, by sampling every
`sampling-interval` seconds (default 10<sup>6</sup> nanoseconds = 1 milli second).

You can view the information being collected, at any point of time using

```emacs-lisp
(profiler-report) ;; or M-x profiler-report
```

The report is a nice, interactive tree with the percentage of time spent in
each call. You can stop profiling by calling `(profiler-stop)`.  If you have
more than one report, you can compare them by hitting `=` in one of the report
buffers.  I'm definitely going to use this for other things! (like speeding up
my startup?)

Now that I have Memacs working with reasonably fast agenda views, I'm looking
forward to collecting as much personal information as I can!  Thanks Karl for
writing Memacs.  I am going to be a pretty heavy user, I think!  There seem to
be a few rough edges, though, and I hope to help smoothen them out a little
bit, over the next few weeks.
