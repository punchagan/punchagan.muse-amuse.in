---
title: "An offline-friendly Elfeed web UI"
date: 2026-01-07T02:31:00+05:30
tags: ["emacs", "blag", "elfeed", "ocaml"]
draft: false
---

I want to read articles from my RSS subscriptions on my phone without signing
up to a hosted service or running a public server.

[Elfeed](https://github.com/skeeto/elfeed), the Emacs feed reader, already lets me manage my subscriptions and read
from within Emacs. It comes with an experimental web UI, but needs the server
(running on my laptop) to be accessible whenever I want to read. My phone
becomes useless the moment my laptop sleeps.

So, I built an alternate web UI with a service worker that caches content on
the client side for a smooth offline reading experience. It's written in [OCaml](https://ocaml.org/)
and compiled to JavaScript using [`js_of_ocaml`](https://ocsigen.org/js_of_ocaml/latest/manual/overview).


## Why bother with RSS feeds? {#why-bother-with-rss-feeds}

It is annoyingly easy to fall into the trap of short form videos or other
algorithmically "curated" feeds and get sucked into scrolling mindlessly. I
fear this is going to get even worse with all the generative AI stuff.

I want to be more deliberate about what I consume. RSS feels calmer and gives
me a greater sense of control. Or it may just be nostalgia from good old Google
Reader days.


## Why Emacs and Elfeed? {#why-emacs-and-elfeed}

Since Google Reader was killed, I've bounced between many readers but none of
them has really stuck with me. I've had [different phases]({{< relref "elfeed-hook-to-fetch-full-content" >}}) of using Elfeed, over
the years, though.

I like the fact that everything is local with Elfeed -- no hosted services, no
public servers. And since it lives inside Emacs, everything from tagging to how
entries are displayed can be tweaked.


## Why Elfeed offline? {#why-elfeed-offline}

Elfeed also ships a basic web UI that lets me read my feeds from a different
device, but only when my laptop is online and reachable. I'd like to be able to
read these posts even when I'm "on the road", say, while waiting for a train or
while taking a cab ride.

I knew it should be possible to do this with some client side caching. And, I
considered improving the web UI of Elfeed itself but it doesn't seem to be
[actively maintained](https://github.com/skeeto/elfeed/pulls) in the last couple of years. Creating a separate project
would also give me more freedom to experiment.


## How does it work? {#how-does-it-work}

Elfeed offline comes with a tiny [Dream](https://camlworks.github.io/dream/) based webserver that acts as a proxy in
front of the Emacs Elfeed webserver for the API requests. The Dream web server
also serves the static assets like the HTML, JavaScript, stylesheets and the
Service Worker for the web app. The diagram below shows how data flows between the different components.

```artist
+---------------+     +-----------------+
|  Emacs Elfeed |<--->|     Dream       |
|     Server    |     |   Web-server    |
+---------------+     +-----------------+
                               ^
                               |
                               v
 +------------+        +----------------+       +---------+
 |    Web     |        |    Service     |       | Browser |
 |  Client    |<------>|     Worker     |<----->|  Cache  |
 +------------+        +----------------+       +---------+

```

The Service Worker intercepts all the `GET` requests from the client and
responds using a [cache-first-with-cache-refresh](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching#cache_first_with_cache_refresh) strategy. This makes the
reading experience feel very responsive. The web client also implements a "good
enough" clone of the original search functionality of Elfeed to allow searching
and filtering content while offline.

The web app also lets me mark entries as read or star them when I'm offline.
The Service Worker caches these operations and updates the server when the
server becomes reachable. There's no smart conflict resolution here, and the
API requests just overwrite and update the state on the server.

I have been using this for a couple of weeks now, and am quite happy with how
responsive the UI feels and the number of posts I managed to read so far.

But, there are definitely some rough edges to smoothen out.

-   It's a pain to make sure that both the servers are running when I'm online
    and want to sync new updates to my phone. I'm considering adding a tiny Emacs
    helper to manage this.

-   I need to remember to open the app on my phone to trigger a cache update
    before stepping away from my laptop. I want to explore using the [Background
    Sync API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API) (not available on Firefox) to possibly make this easier.

-   The UI could use some improvements to indicate pending syncs when offline and
    also indicate the last sync with the server to help ensure everything is
    synced before stepping away from my laptop.

-   Service workers need the server to be accessible via https. I have a wrapper
    script around mkcert to make this easy, but some apps on my phone [refuse to
    work](https://www.reddit.com/r/UPI/comments/1p4le9x/what_happened_to_my_bhim_app/) correctly when there are user installed certificates.


## Why OCaml? {#why-ocaml}

At work, I write OCaml every day and enjoy it. This project seemed like a good
one to try out `js_of_ocaml` since everything is local and I don't need to
worry about bundle sizes, etc.

`js_of_ocaml` makes it quite convenient to share code between the server and
the client side. And given there's also a "third" Service Worker component in
the mix, I thought it would make life easier. For instance, the message types
and the serialization code for the messages between the client and the service
worker are shared.

I'm also using this project to experiment with Dune's "soon to be released"™
[package management](https://dune.readthedocs.io/en/stable/tutorials/dune-package-management/index.html) that our team at Tarides is working on building.


## How can you use it? {#how-can-you-use-it}

You can try out Elfeed offline's UI [here](https://elfeed-offline.muse-amuse.in/) as a static site (with some posts from
Planet Emacslife and The OCaml Planet). You should be able to read posts,
search and filter for posts, mark them as read or star them. Any changes you
make should be preserved between reloads.

If you are an Emacs user but don't use Elfeed, you can checkout the [Elfeed's
README](https://github.com/skeeto/elfeed) for instructions to set it up. It also has links to a bunch of blog
posts and videos that show off the features of Elfeed.

If you are already using Elfeed, you should be able to set it up quite easily
if you're happy installing some OCaml tooling. The installations instructions
are available in the [README](https://github.com/punchagan/elfeed-offline/blob/main/README.org).


## Outro {#outro}

I have been enjoying using Elfeed offline for the past couple of weeks. And I'm
hoping I'll end up spending much more time reading in it, than fixing and
building it. It currently definitely feels like something I built for myself,
but I'd love to hear from others who try it out.
