---
title: "An innocent query that caused Zulip downtime"
description: "Some notes on the changes I made recently, that caused Zulip cloud to be down for a while"
date: 2020-05-28T11:34:00+05:30
tags: ["blag", "zulip", "python", "software"]
draft: false
---

## Introduction {#introduction}

Recently, [a change](https://github.com/zulip/zulip/commit/8f32db81a1a1230b425aef8f7c6d2b7fc4543ee7) that I contributed caused some downtime on the Zulip cloud
(zulipchat.com). Here's a user [tweeting at us](https://twitter.com/zulip/status/1255005502599131137), about this.

I shared this with some friends (who use Zulip) and they asked me to share more
about what happened. I began writing an explanation, and it eventually turned
into a blog post. The post tries to explain what caused the down-time, without
assuming too much knowledge of the Zulip DB schema, but it would help if you
used Zulip a little.

The goal of my change was to change how Zulip backend calculates the
`furthest_read_time` for a user -- the time stamp indicating when the last
message was read.

Previously, the code used simply kept track of the message ID of the messages
being read by a user in a field called the "pointer". My change was to move away
from this `pointer` approach to using the actual timestamp of when a user last
read a message.


## What is the pointer? {#what-is-the-pointer}

Put very simply, the pointer is just a message ID[^fn:1] -- ideally, the ID of the
"last message" a user has read. Message IDs in Zulip are incremental -- a
message that has arrived after another one, would have a higher ID than the
older message. So, it would've been a great way to keep track of the last read
message, if all the messages were in "one continuous feed". But, guess what,
Zulip has streams and topics which are precisely what make Zulip such a valuable
communication tool!

The pointer can be set to the ID of the message that is currently being read,
but only when we are in the "All messages" view. In this view, all messages are
ordered chronologically, so any message that is after another message would have
arrived after it, and would have an ID greater than the other message. So
reading a message in this view means, any message with a lower ID must've
already been read.

When you are reading messages in a stream/topic (narrowed) view, the `pointer`
is not updated. We can't be sure that all messages with ID lower than the
current message's ID have already been read. There could be a whole bunch of
unread messages in other streams/topics than the current one you are reading.
So, the `pointer` doesn't get updated until you go to the "All messages" view
and scroll over the messages, even if you have already read them in a narrowed
view.


## Why change this? {#why-change-this}

Using the `pointer` to compute the `furthest_read_time` doesn't work very well,
because it is only updated in the "All messages" view. In other words,
`furthest_read_time` turned out to actually mean something like
`furthest_read_time_in_all_messages_view`.

The `furthest_read_time` is used in the UI to display the bankruptcy banner -- a
prompt shown to a user to mark all messages as read, if they have "too many"
unreads, and haven't read new messages in the last 48 hours.

But, this is a problem, especially in Zulip instances with a lot of traffic,
where people leave a lot of messages unread until they have the time to
catch-up. It is common for people to communicate only in a handful of
streams/topics, and leave a lot of messages unread in other streams or topics,
that they are hoping to catch-up on, when they have more time at hand. Such
users would avoid using the "All messages" view at any cost.

Even in not-so-high-traffic realms, some users just prefer not to use the "All
messages" view, and just stick to narrowed views.

So, for these users the `furthest_read_time` would get updated very rarely, and
could potentially remain at a date way back in the past. This meant the users
would see the bankruptcy banner despite actively participating in the Realm,
even if only in a few topics/streams. This is annoying UX, and what something we
wanted to fix.


## What did we change this to? {#what-did-we-change-this-to}

We decided to use the last read message time as the message to consider for the
`furthest_read_time`. The following "innocent looking" query should do that for
us, we thought...

```python
UserMessage.objects.filter(user_profile=user_profile, flags=UserMessage.flags.read).last()
```

Well, it does, but not without bringing down the whole of `zulipchat.com` after
a deploy! 🙈 But, why?!

Some background on how data is stored would be useful to see why.


## UserMessage table is huge, my friend {#usermessage-table-is-huge-my-friend}

Zulip's data model has a `Message` table that stores the content of each
message, when it was sent, by whom, to which topic, etc. The `UserMessage` table
is then used to keep track of what the status of this message is, for each user
that has received the message.  A 32 bit flag field is used to keep track of
things like, whether the user has read a message, starred a message, has been
mentioned in a message, etc. So, if a messages is sent to a stream with N users,
it creates 1 row in the `Message` table and N rows in the `UserMessage` table.
If M such messages are sent, it would create M\*N rows in the `UserMessage`
table. So, pretty soon, the `UserMessage` table becomes huge!&nbsp;[^fn:2]

To make common queries on this table efficient, the DB has indexes for them.
Some of the indexes on the `UserMessage` table are documented [here](https://zulip.readthedocs.io/en/latest/production/expensive-migrations.html#running-expensive-migrations-early), though the
documentation was created in the migration context for production deployments.
There are indexes for various things, including **unread** messages.

And here's our innocent looking query, as a reminder.

```python
UserMessage.objects.filter(user_profile=user_profile, flags=UserMessage.flags.read).last()
```

This query searches through the `read` messages for a particular user, and tries
to figure out the last message they read. Note that the DB only has indexes for
unread messages, not read messages! So, this query isn't using DB indexes to
search for this needle in the haystack, and ends up being pretty damn slow!

Additionally, this query is run for every user when the "home page" is loaded
since we want to calculate their `furthest_read_time` to decide if should show
the bankruptcy banner.

Also, Zulip's architecture is designed to allow using the same app server and DB
to host multiple different realms. And zulipchat.com is such a deployment where
a few servers are used to serve all the realms. (I don't know too much about the
deployment setup, though).

When a new change is deployed to zulipchat.com and the server is restarted, all
the clients of all the users reload. Having an expensive query in that path,
would just kill the DB. And this innocent looking query [didn't disappoint](https://twitter.com/zulip/status/1255005502599131137)!


## How did we fix this? {#how-did-we-fix-this}

Well, this change was [reverted](https://github.com/zulip/zulip/commit/976e554799a03ff9d82d7b75d77d45985cd25df4) immediately by [Tim](https://github.com/timabbott), and things were kicked back
into a usable state.

Later, we decided to take a different approach. We decided to look at a
different table (`UserActivity`) that tracks user activity, mainly for the
purpose of analytics. This table keeps track of the last time a user performed
an action based on the API calls made.

Among other things, changing any of the flags in the 32-bit flag field is one of
the actions that is tracked. Marking a message as read was being tracked too. We
use the last time this action was performed to compute the last time a user was
"active", and based on that decide if we should show the bankruptcy banner or
not.

Here's the [actual commit](https://github.com/zulip/zulip/commit/ded3b0076070365dddccd43d7f05fd627c2637f7) that makes this change. But, it turns out that needed a
[follow-up fix](https://github.com/zulip/zulip/commit/734d651b45542e9a1bdea10cd290637f73be30d9) too. 🙈

<div style="font-size:small;" class="reviewers">
  <div></div>

Thanks to [Tim Abbott](https://web.mit.edu/tabbott/www/) and [Shantanu](http://baali.muse-amuse.in) for reading drafts of this post.

</div>

[^fn:1]: The pointer was used to do a [bunch of useful things](https://zulip.readthedocs.io/en/latest/subsystems/pointer.html), but we are currently in the process of [removing it](https://github.com/zulip/zulip/issues/8994).
[^fn:2]: Zulip's code base uses a concept called [soft-deactivation](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#soft-deactivation) to mitigate this problem on Realms where there are a lot of users who log in very infrequently, or don't login after an initial period of activity. So, the number of rows are not exactly `M*N` in all the cases, but in the worst case they are.
