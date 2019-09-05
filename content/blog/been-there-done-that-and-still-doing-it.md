---
title: "Been there, done that, and still doing it!"
description: "Screwing up is a part of the job. Acknowledge mistakes, fix them, improve systems to prevent them."
date: 2019-09-05T12:23:00+05:30
tags: ["software", "management", "learning", "workplace", "blag"]
draft: false
---

I was talking to a friend a few days ago about a new internship she got. She
wasn't sure if and how much she was going to get paid for it. Unpaid internships
aren't cool, and experience doesn't pay the bills, [as they say](https://twitter.com/aoc/status/1154466530500812800). Eventually, it
turned out that she was indeed going to get paid for it.

But, when she found out that she'll be paid, she felt way more pressure to "not
screw up". I think working in this mode of "don't screw up" isn't very productive.
Staying in the mindset of "learn as much as I can" would still be the best way
to go about the internship.

Screwing up is a part of the job. People make mistakes and learn from them.
Screwing up is a part of gaining experience, and learning. To let people feel
comfortable and safe while they are learning, it's important to have better
fallback and recovery mechanisms when things go wrong. The productivity gains
are worth investing time into such systems.

I'm going to write down a couple of times I screwed up -- one of them in my very
first job after college, and the other just a month or so ago. People screw up
every day, irrespective of how much experience they have.


## Corrupted a server's hard-disk {#corrupted-a-server-s-hard-disk}

In my [first job](https://python.fossee.in/), I had screwed up big time in the first couple of weeks of my
job. It's been a while, and a lot of the details escape me now.

I was supposed to resize partitions on a server's hard disk so that there's more
space available for the media that we were going to store on the server. The
server was pretty newly setup, and there wasn't all that much data on it, but my
bosses ([Asokan](https://in.linkedin.com/in/pasokan) and [Prabhu](https://www.aero.iitb.ac.in/~prabhu/)) had spent some time on configuring it, and setting up
user accounts, etc., for all the people that were going to join the project.

I tested the resize operation on a machine locally in the office that I worked
in, and it seemed to work. I replicated this on the server, and it went kaput!
All the data was lost and I could no longer SSH into it. I was totally freaking
out!

But my boss ended up being really calm about it, and asked me to just write to
the server hosting service to get a new machine with a bigger media disk. And
no, I didn't get fired from the job. I worked with him for 5-6 years after that,
including being hired again at a company he started working for.


## Almost Deleted 7-8 years of email {#almost-deleted-7-8-years-of-email}

A few weeks ago, I screwed up again. It could've been pretty bad, but luckily
for me it wasn't.

I administer a [legacy Google Suite](https://support.google.com/a/answer/2855120?hl=en) for [UPAI](https://indiaultimate.org). We have only 10 email IDs to
allocate, and we often recycle them. Recently, I had to merge 3 accounts into a
single one to free up 2 new accounts. I transferred data from two of them to the
third, and went ahead and deleted them. I did this with a couple of other email
accounts before, but they were barely used and nobody really cared about them.

I hadn't paid attention to what data gets transferred, and what doesn't. It
turns out [emails don't get transferred](https://support.google.com/a/answer/33314?hl=en), and only data in the Google Drive gets
transferred. This meant I had lost years of important email communication for
the organisation. I freaked out!

My "[boss](https://indiaultimate.org/u/manickam-narayanan)" was again pretty calm, and asked me to write to Google to see if I
could get them to restore the data. I looked around, and found that Google
allowed restoring deleted accounts for 20 days! I [restored those accounts](https://support.google.com/a/answer/1397578),
[transferred the email](https://support.google.com/a/answer/6351475?hl=en&ref%5Ftopic=6351498) and then deleted the accounts again.


## Learning from screw-ups {#learning-from-screw-ups}

Learning and improving the systems in-place to prevent such screw-ups is the
best thing that we can do from such screw-ups. Just like a piece of software
gets hardened by bug reports that are acted upon, over the course of time, other
systems can and should too.

As described in this [blog post by GitLab](https://about.gitlab.com/2015/01/23/how-to-turn-screw-ups-to-your-advantage/) on how to take advantage of screw-ups,
acknowledging mistakes, fixing them, and improving the systems in-place to
prevent such mistakes is a good way to go about it.

Systems needn't always be super complicated things, but just a [little bit of
automation](https://punchagan.muse-amuse.in/blog/automation-and-habits/), and even [simple checklists](http://scattered-thoughts.net/blog/2016/01/28/notes-on-the-checklist-manifesto/) go a long way in improving work-flows and
making processes less error prone. Google's recovery mechanism definitely
helped, and gives me confidence to continue working with these user accounts.
Our server had a system admin pretty soon, and he had automated back-ups and the
usual stuff in place, for us!

The way a team deals with mistakes sets the tone for how the team works, takes
responsibility, and feels about working together. I still screw up after working
for about a decade as a developer, and being paid for it. I'm sure I'll continue
to have my screw-ups, even though I'd like to have none. What was nice in both
the cases was the way in which my mentors/bosses reacted, and how calm they were
about the whole situation.

May you have screw-ups that you learn and grow from!

PS: Google's [Data Migration Service](https://support.google.com/a/answer/6351475?hl=en&ref%5Ftopic=6351498) doesn't support legacy Google Suite
accounts, and I ended up using [Got Your Back](https://github.com/jay0lee/got-your-back) to move email from the accounts I
wanted to delete to the other accounts. It worked pretty smoothly!

<div style="font-size:small;" class="reviewers">
  <div></div>

Thanks to Aishwarya, Meghana, [Tejaa](https://twitter.com/cst2bicycle/) and [Shantanu](http://baali.muse-amuse.in) for reading drafts of this
post.

</div>
