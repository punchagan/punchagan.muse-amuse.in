---
title: "Software development practices for sports teams"
description: "Some software development practices that sports teams could adopt to be better teams"
date: 2018-09-23T11:31:00+05:30
tags: ["blag", "programming", "ultimate", "hack", "sport", "teams"]
draft: false
---

## Motivation {#motivation}

A few weeks ago, I came across [a talk on Mob programming](https://www.youtube.com/watch?v=SHOVVnRB4h0) --- a technique for
working on a software project as a team, that was accidentally discovered by a
team trying to figure out how to work well together. The speaker lets us in on
how they stumbled on it, and how they fine-tuned it to make it more effective
while being relaxed and enjoyable.

A few days before that, I shared [a post](http://daydreamsinruby.com/getting-feedback/) on "getting feedback (as a software
developer)" with my [Ultimate Frisbee](https://www.youtube.com/watch?v=zEKnqFBajiI) team-mates and it seemed to resonate with
them. I'm often looking at things happening in my sports team from a software
guy's perspective, since I spend a lot of time being the software guy. But, I
rarely, if ever, directly share these thoughts and ideas with my team-mates.

But, the mob programming talk inspired me to make a conscious effort to look for
software development patterns that could be adopted by [our (sports) team](https://thatteidlikaalsoup.team/).

Most players on our team have been playing Ultimate for a while now (2-5 years).
So, we have more problems due to miscommunication and everyone not being on the
same page, than we have due to lack of skills or knowledge. When someone on the
team does not understand the plan, the whole plan goes for a toss.

How do we make sure that everyone understands what the team is trying to do and
is able to contribute their bit to the team's plans and success? How do we make
playing with each other as enjoyable as it can be?

> "The object isn't to make art, it's to be in that wonderful state which makes
> art inevitable." --- Robert Henri


## Some ideas for adoption {#some-ideas-for-adoption}

Here are some ideas that, I think, could be adopted by our team. Some of these
are things that teams, including ours, do in some shape or form. But,
identifying and naming would make it easier for people to talk about them and
develop a common understanding of why and how to do them.


### Ubiquitous Language {#ubiquitous-language}

Eric Evans, in his book Domain Driven Design, talks about building a [Ubiquitous
language](https://martinfowler.com/bliki/UbiquitousLanguage.html) in the team. It grows as the team's understanding of the problem grows,
and helps the team communicate clearly throughout the development cycle.

Our team plays a lot of zone defense, and it usually works well for us But, it
wasn't working particularly well, during one of the tournaments last year.
Luckily, we had [Moby](https://www.instagram.com/monsieurmoby/) playing with us, and he asked us some probing questions
around the objective of the play and the roles of each of the players. With just
a short chat and a few small adjustments, the zone became way more effective.
Essentially, we built a common understanding of the objective of the defense and
brought everyone onto the same page.

Ultimate teams use a lot of lingo -- a lot. New players just pick it up by
osmosis, at practice, from the senior folks. This works most of the time, except
when it doesn't. Each person on the team has a slightly different understanding
of what a term means, and the difference is sometimes big enough to cause a plan
to fail due to miscommunication. Spending time building a common understanding
would make the team communicate and operate more effectively. Practicing game
scenarios is essentially a way of doing this, but it would be worth thinking
about and discussing the terms and the language being used.

Off-field lingo should also be clarified using a similar process -- for
instance, what does "good sideline support" mean? What does giving or not giving
"feedback on the field" mean?


### Sprints {#sprints}

Agile development recommends continuous development of software. Often software
teams use 2-4 week development cycles, called [sprints](http://wiki.c2.com/?ScrumSprint). For each sprint, the team
sets itself a goal, and the whole team prioritizes tasks and makes decisions
in-line with this goal.

Sports teams would also benefit from sprints -- short and focused practice
cycles, where everyone on the team is aware of the team's goal. This would make
it much easier for players to help each other out. Also, players can align their
individual goals with the team goal, making practices much more effective.


### Retrospectives {#retrospectives}

> At regular intervals, the team reflects on how to become more effective, then
> tunes and adjusts its behavior accordingly. --- The Agile Manifesto

Most Ultimate teams do some kind of post-practice retrospectives, though, they
don't call it that. These retrospectives are a discussion of the good, bad and
the ugly. Usually, no conscious decisions are made about what practices are
working well for the team, and what should be taken forward to upcoming ones.

Slightly longer term retrospectives would be quite useful too. If a team adopts
the idea of sprints, each new sprint should start with a retrospective of the
last one and planning for the next.

A retrospective's participants are expected to follow the [prime directive](http://retrospectivewiki.org/index.php?title=The%5FPrime%5FDirective).

> Regardless of what we discover, we understand and truly believe that everyone
> did the best job they could, given what they knew at the time, their skills and
> abilities, the resources available, and the situation at hand. --- Norm Kerth,
> _Project Retrospectives: A Handbook for Team Review_

Internalising this would be really helpful especially during post-tournament
retrospectives, where emotions can run high -- it would keep the discussion
positive and focused on identifying problems and finding solutions, rather than
spiraling into blame games, defensive arguments, etc.


### Daily Stand-ups {#daily-stand-ups}

Agile teams [gather each day](https://www.mountaingoatsoftware.com/agile/scrum/meetings/daily-scrum) at the start of the work-day, to let each know about
the progress of the work-items. The team tries to help each other get rid of the
impediments to progress.

Ultimate teams could also benefit operating in this style -- everyone shares
with each other what they are working on, and the problems in their learning.
This would make it easier for others to look out for things to help with.
Team-mates would limit themselves to giving feedback to the thing that a player
is working on.

Players setting themselves a small number of clear focus points would also force
them to consciously think about and work on their game more effectively.


### Face-to-face communication {#face-to-face-communication}

> The most efficient and effective method of conveying information to and within a
> development team is face-to-face conversation. --- The Agile Manifesto

As our team has grown larger over the years, more and more communication has
moved to the WhatsApp group. Keeping everyone informed via face-to-face
communication, at this team size needs a lot of co-ordination and planning, and
the time at practice is considered to be too precious to be spent talking and
not practicing.

But, clearly WhatsApp doesn't seem like the best medium to have discussions.
Discussions rarely, if ever, happen on our groups. It often just seems to be
information dissemination. Using a [better communication tool](http://zulipchat.com/hello) could mitigate a
few of these problems, but face-to-face discussions have other benefits. They
bring about a greater sense of belonging to the team and increase buy-in into
the team's plans.


### Unit tests vs. Integration tests {#unit-tests-vs-dot-integration-tests}

Practice games are helpful to gauge if a team is playing well together and if
its plans are working. This seems analogous to [integration tests](http://wiki.c2.com/?IntegrationTest) --- checking
that we have functional software, end-to-end.

But, in the early stages of development, it's common to write [unit-tests](http://wiki.c2.com/?UnitTest) --
tests to ensure that each of the individual components works well in isolation.
An analogous thing would be to have individual evaluations to help players
identify weak areas, and to measure progress in those areas. It would also
prevent players from slipping on important "indicators".


## Other ideas to think about {#other-ideas-to-think-about}

Some ideas that I find interesting, but don't yet know if and how they can be
adopted by sports teams are below.


### Mob programming {#mob-programming}

In a [mob programming session](https://www.agilealliance.org/resources/experience-reports/mob-programming-agile2014/), everyone on the team is working on the same
computer, in the same room, at the same time. This seems tremendously
ineffective at the face of it, but turns out to be a good way to produce high
quality software, quickly.


### Hammock driven development {#hammock-driven-development}

Bugs are incredibly expensive to be found and fixed in production software. They
are cheaper to fix in the development phase. But, the design phase is the best
place to fix them.

Rich Hickey [recommends](https://www.youtube.com/watch?v=f84n5oFoZBc) feeding a lot of information about the problem you are
trying to solve to your waking mind, so that your background mind can feed off
of it while you are asleep, and make useful connections.


## Conclusion {#conclusion}

> Build projects around motivated individuals. Give them the environment and
> support they need, and trust them to get the job done.  --- The Agile manifesto

This sounds exactly like what players in our team need too. The captains and the
mentors in the team should work towards providing the environment and the
support everyone on the team needs, and trust them to do the job.

<div style="font-size:small;" class="reviewers">
  <div></div>

Thanks Meghana Iyer, [Ravitheja Tetali](https://twitter.com/cloud9trt/), [Shantanu Choudhary](http://baali.muse-amuse.in/), [Vandith PSR](https://twitter.com/vandith), [Varun
Rangarajan](https://varunrn.wordpress.com/) and Vivek Krishnaswamy for reading drafts of this post and giving
helpful suggestions.

</div>
