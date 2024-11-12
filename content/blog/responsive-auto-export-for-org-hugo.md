---
title: "Responsive Auto Export for Org Hugo"
description: "Improving the responsiveness of ox-hugo's auto export functionality to make writing blog posts a joy again!"
date: 2024-11-13T00:17:00+05:30
tags: ["blag", "emacs", "hack", "writing"]
draft: false
---

I use [ox-hugo](https://github.com/kaushalmodi/ox-hugo/) to [write blog posts]({{< relref "deploying-hugo-drafts-simplified" >}}) in org-mode and publish them using [Hugo](https://gohugo.io/). I
[enjoy using org-mode]({{< relref "why-i-like-org-as-a-markup" >}}) for any writing that I do, including blog posts (when I am
able to get myself to write them). After a long hiatus, I've been trying to get
back to blogging, as this post might have given away. But, ox-hugo's [auto
export](https://ox-hugo.scripter.co/doc/auto-export-on-saving/) seemed much slower than I remember it being.

Each time I hit save on my `blog-posts.org` file, Emacs gets busy for about
10ish seconds exporting the post to Hugo markdown. And this is annoying because
I tend to hit `save-buffer` multiple times while writing in `Emacs` -- thanks,
muscle memory!


## Enter Emacs profiler {#enter-emacs-profiler}

I was on a flight and had some time to dig into this. If I was online, I
probably would have looked through the README and/or the issue tracker, but I
[jumped in]({{< relref "how-i-learnt-to-use-emacs-profiler" >}}) with the handy [Emacs profiler](https://www.gnu.org/software/emacs/manual/html_node/elisp/Profiling.html).

The profiler-report showed that a big chunk of time was being spent in
`org-id-update-id-locations` even before the actual export started. And then,
during the export, a bulk of the time was spent in
`org-hugo--get-pre-processed-buffer`. Once I knew the problem areas, I started
poking around in the `ox-hugo` code to "fix" these issues.


## Turn off Org ID location update {#turn-off-org-id-location-update}

`org-id-update-id-locations` scans a bunch of org-mode files and stores a
mapping of all the IDs of subtrees to their filenames. If you have a lot of org
subtrees this can take a while, even if none of them actually have IDs. It
turns out that I didn't have any ID properties set, and this caused the [update
function to run before every export](https://github.com/kaushalmodi/ox-hugo/blob/98421a1298adc6d80ce21b3cb5c951af818b27bf/ox-hugo.el#L4881-L4882)!

I simply added a new ID property on one of the subtrees in my blog-posts file
to prevent the ID updation from running on every export! I'm not sure how a
stale `org-id-locations` value affects cross links, but at this stage of
writing I don't care about the cross links. (spoiler: The next hack actually
nullifies any impact a stale value might have had!)

Cutting down auto export time by 4-5 seconds is great! But, I'm still not happy
to wait for 5-6 seconds in the middle of writing my posts. Let's look at the
other hotspot -- the buffer preprocessing!


## Turn off buffer preprocessing, maybe? {#turn-off-buffer-preprocessing-maybe}

Currently, I don't have any cross links between posts in my org-mode source.
So, I can turn off this feature completely by setting
`org-hugo--preprocess-buffer` to `nil`. Viola! Hitting `save-buffer` doesn't
freeze my Emacs any more. I can compose "100s of blog posts"™ in a flurry! ;)

But, if I'm going to have these "100s of blog posts", wouldn't it be better to
have cross links? But, with preprocessing turned off when there are
cross-links, the "auto-export and build" workflow breaks. The variable
`org-hugo--preprocess-buffer` MUST be non-nil to produce posts with **valid**
cross-links. If not, the exported markdown file processed by `hugo` ends up
having broken cross-links, which crashes `hugo serve` and/or `hugo build`.

Unsetting and setting the `org-hugo--preprocess-buffer` variable for the
writing vs publishing phase, respectively, isn't an ergonomic workflow. It's
not an improvement over disabling and enabling the auto-export mode as needed.
I want to enjoy auto export with Hugo's [live reload](https://gohugo.io/getting-started/usage/#livereload) feature.


## Moar workaround! {#moar-workaround}

Looking through the code some more, I learnt [`org-hugo-link`](https://github.com/kaushalmodi/ox-hugo/blob/98421a1298adc6d80ce21b3cb5c951af818b27bf/ox-hugo.el#L2723) first uses a
custom export handler, if one exists for a link's protocol. I decided to piggy
back on this functionality and made up `hugo:` protocol for cross-links.

The `hugo` link simply contains the `EXPORT_FILE_NAME` of the linked blog post
i.e., name of the exported markdown file (without the .md extension) as the
'path' of the link. The custom protocol export handler can then generates a
`relref` shortcode for Hugo to process in the exported markdown file.

This nicely works around the need to preprocess my entire `blog-posts.org`
buffer to generate **valid** cross-links!

```emacs-lisp
(org-link-set-parameters "hugo" :export #'pc/org-hugo-link-export-to-md "Export Hugo blog link to markdown file" )

(defun pc/org-hugo-link-export-to-md (path desc backend &optional info)
  "Export a link to a Hugo blog link in markdown format."
  (message (format "path: %s, desc: %s, backend: %s" path desc backend))
  (cond
   ((eq backend 'md)
    (if (equal org-export-current-backend 'hugo)
        (format "[%s]({{</* relref \"%s\" */>}})" desc path)
      (error "Cannot export Hugo link to non-Hugo backend")))
   (t (error "Cannot export Hugo link to non-Hugo backend"))))
```


## Outro {#outro}

I made a [simple helper](https://github.com/punchagan/dot-doom/blob/c45f01e6b20275ce1df943855626af5c40cb626c/config.el#L541-L564) to make it easier to insert these cross-links with the
`hugo:` protocol. It simply looks through all the headlines with an
`EXPORT_FILE_NAME` property, and allows it to be inserted as a link with the
`hugo:` protocol.

Now, cross-linking posts and publishing posts with cross-links are both a
breeze. Stay tuned for the "100s of blog posts" ™ I'm going to write!
