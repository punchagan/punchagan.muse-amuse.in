---
title: "Deploying Hugo Drafts, simplified"
date: 2020-05-31T17:19:00+05:30
tags: ["hugo", "blogging", "hack", "emacs", "blag"]
draft: false
---

This is a follow-up post to my last post, [Deploying Hugo Drafts](/blog/deploying-hugo-drafts). Kaushal Modi,
the author of [ox-hugo](https://github.com/kaushalmodi/ox-hugo) (a tool that lets you compose in org-mode and use Hugo to
export), let me know about the [build options](https://gohugo.io/content-management/build-options/) in Hugo.

{{<tweet 1266761525286653952>}}

The build options in Hugo let you configure building a post for different use
cases like render a post but hide it in lists, or don't render separate pages
for posts and only show them in lists, etc.

To use these build options for my use case -- being able to share draft post
links with friends, without them appearing in the index page or RSS feed -- I
just need to add the following to my draft blog posts!

```conf-toml
_build:
  render: true
  list: false
```

But, how do I do this with `ox-hugo`? I know `ox-hugo` doesn't yet have this
feature, for sure, because Kaushal mentioned that he hasn't tried it out yet.

I checked to see if I could use the `EXPORT_HUGO_CUSTOM_FRONT_MATTER` property
to get it to generate this extra metadata for each blog post. But that didn't
work. The property assumes all the arguments to it are top level front matter
keys and values, which is good enough for "normal" use cases.

It could potentially be a useful contribution to `ox-hugo` to allow configuring
the build options for a post, but there's an easier way out for now, thanks to
the cascading of these build properties to children. Here's how I set that up:

I created a `drafts` folder in my hugo `content` directory, and added the
following content to an `_index.md` file in it.

```conf-toml
title: Drafts
_build:
  render: false
  publishResources: false
  list: false
cascade:
  _build:
    render: true
```

The `_build` properties get cascaded to the children -- any files created in
that directory -- and the properties under `cascade` overwrite the inherited
properties. In other words, the configuration above would translate to adding
the following to _every draft post_:

```conf-toml
title: A How-to on Hugo Drafts
_build:
  render: true
  publishResources: false
  list: false
```

Now, I just need to make sure that all my draft posts are created in this
`drafts` directory. `ox-hugo` allows doing this by simply using the
`EXPORT_HUGO_SECTION` property on my post subtree. I added this additional
property to my helper function that I use to create hugo blog posts from any
subtree.

```org
* DRAFT A How-to on Hugo Drafts :blogging:hack:
:PROPERTIES:
:EXPORT_FILE_NAME: how-to-hugo-drafts
:EXPORT_HUGO_SECTION: drafts
:EXPORT_DATE: [2020-05-31 Sun 16:51]
:END:
```

I'm now all set to publish draft posts without requiring to use `rsync` and two
`hugo` builds. :) Publishing a draft post would need me to remove the `DRAFT`
todo keyword, like before, but additionally also remove the
`:EXPORT_HUGO_SECTION:` property on the subtree. This should be quite quick to
do, or pretty easy to put into an interactive function if required.
