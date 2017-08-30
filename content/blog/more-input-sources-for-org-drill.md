---
title : "More input sources for org-drill"
date : "2014-11-04T00:00:00+05:30"
tags : ["emacs", "hack", "learning", "orgmode"]
draft : false
---

I've been trying to use `org-drill` regularly for the last few weeks.  I don't
know how well it's been going but I have been sticking to the routine
religiously.  I haven't yet really tried out incremental reading, but in an
attempt to make it as easy as possible, I wanted to have a pdf-reader
integration, and some kind of integration with Kindle highlights.  Browser
integration is pretty straight-forward, thanks to some [simple java-script](http://orgmode.org/worg/org-contrib/org-protocol.html#sec-6).

I looked for a pdf-reader with some sort of plugin support, but I found nothing
in Evince or Okular.  I thought about `pdfjs` but it seemed slightly clunky to
open pdfs in a browser, though I might shift to this if I don't like what I
finally ended up with.  Good old `xpdf` seemed to be the only pdf reader that
had some support for custom keybindings that allowed users to run external
commands.  With a [little Python](https://github.com/punchagan/dot-emacs/blob/master/xpdf-capture), I was able to setup a work-flow to capture
snippets from `xpdf`, to add to org-drill. Custom key-bindings somehow don't
seem to work on `xpdf` bundled on Ubuntu. So, I ended up downloading and using
the binary available on the xpdf site.

For Kindle highlights support, with minor updates to Thamer Mahmoud's [clip2org](https://github.com/punchagan/clip2org),
I have a simple way of getting all the "new" clippings/highlights as org-drill
headlines.  I haven't really started using this, and once I do, I may end-up
automating even the merging of these items into the org-drill notes file.  I'm
looking forward to making better use of my Kindle, with this feature!

I don't know if it would be useful to have more context information like
section titles/chapter titles when capturing from html/pdf, but it seems like
an interesting problem to try to solve.

Also, it might be easier(?) if I probably tried to have a DE level keybinding, and
some code to get selection and file name of the currently active
window/application.
