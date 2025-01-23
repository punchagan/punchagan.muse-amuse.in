---
title: "Some useful Git configuration for Windows"
date: 2025-01-24T01:25:00+05:30
tags: ["git", "blag", "windows", "til"]
draft: false
Some: "useful git configuration for windows that I learnt"
---

I've recently been working on Windows with a relatively involved git repository
and ran into a bunch of issues. Setting these configuration values turned out
to be very helpful!

```sh
# Allow symlinks
git config --global core.symlinks true

# Don't automatically change file endings to \r\n (carriage return + line feed)
git config --global core.autocrlf false

# Use line feed for line endings
git config --global core.eol lf

# Allow long paths in the repo
git config --global core.longpaths true
```

It's also useful to set these as configuration values in `.gitattributes` in a
repository to share this configuration with other people working on it.


## Related posts {#related-posts}

-   [Git resources]({{< relref "git-resources" >}}) : A post with some resources to better understand git, along
    with some useful git configuration.
