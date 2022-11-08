---
title: "Moving from Heroku to Fly.io"
description: "How I moved a couple of apps from Heroku to Fly.io"
date: 2022-11-06T12:19:00+05:30
tags: ["heroku", "python", "hack", "blag"]
draft: false
---

A couple of months ago Heroku [announced](https://blog.heroku.com/next-chapter) their plan to "Focus on Mission
Critical" and shut down the free product plan. The ideas is to free up their
developer time to focus on the important stuff instead of fighting abuse of the
free plans. I'm surprised they invested in the free plans for so many years!


## My Heroku Apps {#my-heroku-apps}

I have a bunch of apps on the free (Hobby dev) plan, and only app on the Hobby
Basic plan because it needed a bigger DB. All of these apps are small enough
that I could easily host all of them on my shared [Hetzner server](https://www.hetzner.com/), where this
blog is hosted. But, I like using Heroku for services that I run for other
people. It makes access control and deployment much easier, and lets me invite
other people to help maintain apps easily, despite constraints like [10k rows](https://devcenter.heroku.com/articles/heroku-postgres-plans#hobby-tier) in
the Postgres DB and [Dyno sleeping](https://devcenter.heroku.com/articles/free-dyno-hours).

Over the years of using Heroku, I ended up accumulating a bunch of small apps
on the service. Most of these apps aren't actively being used any more and
didn't feel worth the effort of moving.

I decided to let most of the apps die, since they aren't actively being
used. Only a couple of apps are used regularly enough to be worth keeping alive
-- [SOTG Calculator](https://sotg.indiaultimate.org/) and [RSVP app](https://rsvp.tiks-ultimate.in/features). I turned on [maintenance mode](https://devcenter.heroku.com/articles/maintenance-mode) on the RSVP app
for a couple of days, as an experiment, and I had to bring back the services
due to "popular" demand.


## Why not pay Heroku? {#why-not-pay-heroku}

I did consider just moving up to the Hobby basic plan and paying for running
the app. I wasn't keen on investing numerous hours to get these apps to run
again. [Akilesh](https://instagram.com/akilesh.m) convinced me that the amount to pay Heroku could be collected
from the team and wouldn't amount to much per person. I almost took this route.

But, it bugged me that the amount we'd be paying Heroku could fund a couple of
turf practice sessions for the team. I could host the apps on my Hetzner server
-- we already pay enough for it. But, giving other people maintainer access to
apps is important and this was not straightforward with Hetzner.

Also, the SOTG app couldn't be funded this way.


## Why Fly.io? {#why-fly-dot-io}

I ranted about this to my friends on Zulip and [Rajesh](https://github.com/rajaboja/) offered to help me as a
way to learn some devops stuff. I was more than happy to have someone to
discuss this stuff with and get some help.

We decided to give [Fly.io](https://fly.io/) a try despite being skeptical about using yet another
free service. Their free Hobby plan includes 3GB of persistent storage space
(which neither of the apps currently use, but potentially could). They also
built [Turboku](https://fly.io/blog/new-turboku/) -- a tool to move apps from Heroku. It seemed worth giving a try,
and we could always fall back on Hetzner if it didn't work out.

We had a couple of months before the Heroku shutdown date, when I ranted about
this. Rajesh and I exchanged a few links and messages on how to potentially go
about doing this, when we got down to it. But, he got busy with other things
and now the deadline was only a month away. I decided to use the notes and do
the migration myself. I was glad I had the notes to refer to. The initial
"research" made the task seem less daunting.


## Migrating a simple app {#migrating-a-simple-app}

I started with the simpler app first -- the [SOTG app](https://sotg.indiaultimate.org/). I used the [Turboku web
page](https://fly.io/launch/heroku) and it worked pretty seemlessly! It copied over the environment variables
from Heroku and deployed the app.

But, using the Turboku web page meant that I didn't have a `fly.toml` file to
do any future deployments. I used the `fly launch` command to create a new app
and edited the `fly.toml` file to point to the migrated app.

Setting up the custom domain was pretty simple too, using the CLI. I just had
to run `fly certs add sotg.indiaultimate.org` after changing the DNS entries to
point to `sotg-calculator.fly.dev`.

The whole thing felt quite simple and I was done in under an hour -- reading
the docs, installing the tool, trying out different things, getting it all
working. Everything. Quite impressive!


## Migrating a bigger app {#migrating-a-bigger-app}

Encouraged by this, I started with the RSVP app. I didn't think it would be
much harder than this, but I guess when there are a few more moving parts, it's
hard to tell what could pop-up.

I used the same approach for the migration -- Turboku web page to migrate from
Heroku and then ran the launch command to generate a `fly.toml` file that I
edited to point to the deployed app.

The deployment seemed to go fine, but the app wouldn't come up. I looked at the
logs to find out that the app was getting [OOM killed](https://neo4j.com/developer/kb/linux-out-of-memory-killer/). Fly.io provides half the
memory (256MB) that Heroku provided. But, I wasn't expecting this tiny app to
need much more.

I removed some default imports of large packages, but it didn't really help
that much. I did consider reducing the Gunicorn's `WEB_CONCURRENCY` setting to
1, but didn't want to take that route unless absolutely required. I looked
around the forums a little, and [found](https://community.fly.io/t/question-about-weird-deployment-size-on-fly/5677/2) that using a Dockerfile instead of the
buildpacks might improve the memory situation. And it did!

Next, I moved to setting up the custom domain and it worked from the Fly.io
side seemlessly. But, the `flask_dance` library was generating `http` URLs in
it's OAuth redirect URLs. The app already uses FlaskSSLify, but that didn't
seem to be sufficient. After reading some [Flask dance](https://flask-dance.readthedocs.io/en/latest/proxies.html) and [Flask](https://flask.palletsprojects.com/en/latest/deploying/proxy_fix/) docs, I found
that Werkzeug's `ProxyFix` exists exactly for this!

After dealing with these two unexpected problems, I got to the problem that I
was aware I had to tackle -- Fly.io doesn't have support for cron jobs. The
RSVP app uses some scheduled jobs to periodically sync some metadata from
Google Drive, Calendar, etc.

I took a hackish route to work around this. Using the [schedule](https://schedule.readthedocs.io/en/stable/) library, I wrote
a ["cron" script](https://github.com/thatte-idli-kaal-soup/rsvpapp/blob/master/scripts/cron.py) that would run the jobs on the desired schedule. I created a
duplicate app to run the cron service, even though it could potentially be run
as a different process on the same app. I didn't want to risk any more OOM
kills on the web app. But, it can be a little bit more work to keep the
environment variables and other such things in sync between the two apps.

I was quite excited about Fly.io having a datacenter in Madras and was swayed
by Fly.io's marketing about running the app close to the users. I tried this
but the performance was terrible since the Mongo DB was in North Virginia. I
quickly switched back to using an East Coast region for Fly.io app too.

But, while writing this blog post, I realized that I could move the DB to
India. I moved the DB to the AWS Mumbai datacenter, and the Fly.io app to the
Madras datacenter.


## All's well that ends well {#all-s-well-that-ends-well}

The app has been chugging along for a few days without any new hiccups. I'm
hoping things stay this way for the weeks and months to come, if not years.

On the whole, I found the whole experience more beta-ish than deploying
something to Heroku. But, I'm quite happy with how the whole thing turned
out. I think things will get smoother with time -- with my growing familarity
with Fly.io and more people using their tools suggesting improvements.

I am wary of depending on yet another Hobby plan, but neither of these apps
make any revenue and I'm not (yet) comfortable charging users for the small set
of features they provide.

I'd like to hear stories of other people moving away from Heroku! Feel free to
reach out!
