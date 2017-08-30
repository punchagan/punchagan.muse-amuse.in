---
title : "Create a Public Jupyter Server, quickly!"
date : "2016-08-25T00:00:00+05:30"
tags : ["blag", "hack", "ipython", "python"]
draft : false
---

I create public Jupyter notebooks once in a while, to collaborate with a
friend, or to make it easier for myself to work with data on a remote machine.

Each time I need to look up the [docs](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html), and manually set-up a few things, before
I can start using the notebook.

I just wrote a bash script that does the following, quickly -

-   Install Jupyter into a temporary virtualenv
-   Create certificate files
-   Start the server with https enabled and a password
-   Delete all temporary files, when the server is shutdown

<script src="https://gist-it.appspot.com/github/punchagan/dot-files/blob/master/bin/jupyter-server.sh"></script>

You can get it [here](https://github.com/punchagan/dot-files/blob/master/bin/jupyter-server.sh), if you'd like to use it.
