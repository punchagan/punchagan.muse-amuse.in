---
title: "Restoring a broken Ubuntu upgrade"
description: "Using chroot to restore a broken Ubuntu system on update"
date: 2024-11-20T15:17:00+05:30
tags: ["ubuntu", "linux", "hack", "blag"]
draft: false
---

A couple of weeks ago, [Shantanu](http://baali.muse-amuse.in) and I were discussing Ubuntu upgrades -- his
upgrade was borked and he ended up re-installing his system. I was celebrating
the fact that I never really had to throw away my OS installation entirely
since I switched to Ubuntu after getting tired of [Arch Linux in 2011-12]({{< relref "numpy-pacman-and-me" >}}).

And on cue, I had a really broken update on my dad's laptop! It was really
broken -- no WiFi, no Ethernet connection, no GUI packages, etc.


## The crash {#the-crash}

I started the update but forgot about it, promptly. My dad was semi-supervising
it, since he was using the laptop on-and-off. I came back to it a couple of
days later, and I ran an autoremove, assuming everything else in the install
went ok. Everything continued to work alright until some time later, we had to
restart the X server because it had hung up. And it never came back. And on a
full restart, no network -- both Ethernet and Wifi.


## `chroot` to the rescue! {#chroot-to-the-rescue}

Thankfully these are not the days when I had [access to a single computer]({{< relref "not-so-floppix" >}}), and
crashing it meant running to a friend and using their computer to download
stuff. I quickly made a bootable USB on my laptop.

I boot my dad's laptop using the live distro and chroot to the installed OS
using the live distro. Live Ubuntu has Ethernet working, thankfully.

For `apt-get install` and `dist-upgrade` to work correctly with the `chroot`, I
had to [mount a bunch of volumes](https://forum.manjaro.org/t/howto-chroot-from-or-into-any-linux-distribution/34071).

Due to some network manager changes in the update, the `chroot` system still
wasn't connecting to the internet. I probably should've looked at the
`resolv.conf` file first, but ended up going the [offline package install](https://wiki.ubuntu.com/OfflinePackageDownload)
route...


## Offline updates {#offline-updates}

I generate a list of missing packages to be downloaded using the `--print-uris`
flag to `apt-get` on the `chroot` system; And use `wget` to download the
packages on the "live" system; Then copying these packages to
`/var/cache/apt/archives/` gets the update to finish.


## But more missing packages! {#but-more-missing-packages}

I rebooted into the installed OS, once `apt-get dist-upgrade` seems to have
everything resolved. But, I still didn't have a network! I had to `chroot`
again into the system, and this time I figured out that there was an issue with
`resolv.conf` being a broken soft-link which seemed to cause the broken network
(with Ethernet).

For WiFi, I had to install proprietary drivers for the Broadcom wireless card
(`BCM43142 802.11b/g/n`).

I had to also install the `ubuntu-desktop` and related packages that seem to
have gone missing, and on reboot everything was up and running!


## Outro {#outro}

When I told Shantanu, I didn't have to reinstall my Ubuntu from scratch doesn't
mean that all my updates were flawless, and things never broke. I have had such
broken updates a few times -- network updates leaving the system in a broken
state after network connections died, Ubuntu upgrade being in a borked state
after the [xz vulnerability was discovered](https://ubuntu.com/security/CVE-2024-3094), etc.

Updates do fail. But, more often than not I've been able to restore things
thanks to `dpkg` 's robustness and awesomness! And in some extreme cases,
reaching for `chroot` to save myself.

There's probably nothing new to learn or discover in this post, but just some
help forum links that might come in handy, in future. In this age of AI
answers, it seemed nice to look through some old forum QAs and work things out
using them.

<div style="font-size:small;" class="reviewers">

Thanks to [Shantanu](http://baali.muse-amuse.in) and [Kamal](https://x.com/kamalx) for reading drafts of this post.

</div>
