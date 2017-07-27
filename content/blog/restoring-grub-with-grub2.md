+++
title = "Restoring GRUB with Grub2"
date = "2010-08-10T00:00:00+05:30"
tags = ["note", "ubuntu"]
draft = false
+++

It's a one liner with grub2.

    $ sudo grub-install --root-directory=/mount/point/of/root/ /dev/sdX

where `sdX` is `sda,sdb,..` depending on which hard-drive it is
on.

This is the first instance when I found grub2 to be better
than grub.
