+++
title = "Recurse Center, 2014-07-03"
date = 2014-07-05T09:49:37-04:00
tags = ["django", "python"]
categories = ["recursecenter"]
draft = false
+++

-   I got distracted trying to add a hack to Hacker School's [blaggregator](https://github.com/sursh/blaggregator), to
    enable posting to different channels on zulip.
-   I learnt a few things about Django.  Commented out references to views that
    don't exists breaks templating.  Formsets didn't seem very convenient to use,
    for editing data showing the user only partial forms.
-   I played around with Clang for a bit, to try and use libclang to parse the C
    code for inspection, instead of writing one myself.  It sometimes feels like
    an overkill, but it feels like it'll make the whole code more robust.  I'm
    not sure.  I'll need to play around for a bit more to decide.
-   I also finally got around to fix the resolution of my tty shells.  I was in a
    bus, and wanted my laptop's battery to last longer, and decided to use a tty
    shell with just emacs running. But, the resolution sucked.  So, I
    fixed. Essentially it involved removing a blacklist file that an old version
    of Nvidia drivers left behind in
    `/usr/share/grub-gfxpayload-lists/blacklist/` and setting
    `GRUB_GFXMODE=1920x1080` in `/etc/default/grub`.
-   Later in the evening I also bought the domain `octo.cat`, given there were a
    bunch of people buying cat domains, and talking about it on Zulip!

Update [7/7/14]: I forgot to write about the presentations.  There were
interesting presentations!

-   [Protagonist](https://github.com/ambimorph/protagonist)
-   [mesh networking](https://github.com/pirate/mesh-networking)
-   [The Execution Context](http://writing.brianruslim.com/2014/06/30/the-execution-context/)
-   [toolmaker](https://github.com/stijlist/toolmaker/)
-   [Building a better doorbot](http://blog.ontoillogical.com/blog/2014/07/03/doorbot-overflow/)
-   [Fredis](https://github.com/buybackoff/Fredis)
