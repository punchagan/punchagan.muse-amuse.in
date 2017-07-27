+++
title = "Using tmux to \"screen share\""
date = "2014-11-24T00:00:00+05:30"
tags = []
draft = false
+++

I wanted to pair with a friend of mine, exploring Magit mode in Emacs.  There
are a couple of projects to make it easy to use tmux(-like) to simplify this.

-   [pairing](https://github.com/non/pairing) lets you share a screen and pair, on a common server where both the
    users have access to.  But I wanted to use my machine, instead of the
    server.

-   [tmate](http://tmate.io) gets around the restriction of having a common server where both users
    have access, but needs a custom install of tmux, and the use of a 3rd party
    service.

I worked around this, using an ssh reverse tunnels.  Here are the steps, for
anyone who'd like to reproduce.

1.  Add your partner(-in-crime)'s ssh key to authorized keys on a server that
    has a public IP (`example.com`, let's say).

2.  Add your server's key to authorized keys on your local machine.

3.  Create a reverse tunnel from your machine to the server.

    ```sh
    ssh -fNR 19999:localhost:22 server_user@example.com
    ```

    `-R 19999` essentially forwards port 19999 on `example.com` to
    localhost's 22.  `-fN` is to say no terminal, send connection to background.

4.  Your partner first ssh's to example.com and then ssh's to your laptop.

    On your partner's machine

    ```sh
    ssh server_user@example.com
    ```

    On the server, your partner does

    ```sh
    ssh your_username@localhost -p 19999
    ```

    Your partner is on your machine, and can run `rm -rf`!  But, hopefully
    they'll only run `tmux attach`.  Obviously, do this only with people you
    trust!

5.  Start a tmux session locally.

6.  Profit!
