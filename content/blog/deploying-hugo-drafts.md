---
title: "Deploying Hugo Drafts"
date: 2020-05-30T19:07:00+05:30
tags: ["blag", "hugo", "blogging", "hack"]
draft: false
---

**Update <span class="timestamp-wrapper"><span class="timestamp">[2020-05-31 Sun 17:23]</span></span>**: I published a [simpler workflow](/blog/deploying-hugo-drafts-simplified) for this, using
Hugo's build options that I wasn't aware of, because they are relatively new.

A few friends and I run a weekly writing club similar to [this](https://github.com/sursh/writing-club). Once we have our
drafts ready, we usually share them for reviews, etc.

Previously, I used to use [Nikola](https://getnikola.com), and it's default behaviour is what worked well
for this workflow -- share the posts URL with reviewers, but the post shouldn't
appear in the feed, post list, etc.

> If you set the status metadata field of a post to `draft`, it will not be shown
> in indexes and feeds. It will be compiled, and if you deploy it it will be made
> available, so use with care. If you wish your drafts to be not available in your
> deployed site, you can set `DEPLOY_DRAFTS = False` in your configuration.

I moved to using Hugo a few years ago. By default, it doesn't publish the draft
posts, but you could ask it to do so using the `--buildDrafts` option. But, that
doesn't do what I want -- draft posts are treated just like any other post, and
they appear in the feeds, post list, etc.

Given how fast `hugo` builds are, though, it is pretty easy to hack-up the
behaviour I want.

1.  Run a build with drafts, say to `dev` directory.

    ```sh
    DEV_DIR="dev"
    # Build drafts to dev dir
    hugo --cleanDestinationDir -D -d "${DEV_DIR}" > /dev/null
    ```

2.  Run a build without drafts, to `public` directory.

    ```sh
    PUBLIC_DIR="public"
    hugo --cleanDestinationDir -d "${PUBLIC_DIR}"
    ```

3.  Copy the drafts from the `dev` build to the `public` build

    ```sh
    rsync -ri --ignore-existing "${DEV_DIR}"/ "${PUBLIC_DIR}"
    ```

4.  Deploy the `public` build

The code above is [here](https://github.com/punchagan/dotfiles/blob/3652a6be42c776c6d1771e6cd46acadb2cafe295/bin/publish-hugo-drafts.sh) as a single script. [Here](https://github.com/punchagan/punchagan.muse-amuse.in/blob/fdc80a61e28290c1c4a48a437bc77ec3fda811f5/deploy.sh) is the full deployment script
for my blog.
