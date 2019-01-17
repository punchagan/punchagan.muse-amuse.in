---
title: "2018 in Review"
date: 2019-01-17T15:02:00+05:30
tags: ["blag", "life", "blab", "annual-review", "ultimate", "programming", "writing", "goals"]
draft: false
---

Here's my review of 2018 - my first successful annual review. I remember wanting
to do something like this, a couple of times before too. This time, I managed to
get started and wrap it up!

I've been inspired to write one by a some reviews that I read this year -- some
of them do it every year.

-   Sher Minn's [visual retorospective](http://piratefsh.github.io/2018/12/25/2018-retrospective.html)
-   Nat's [month-wise review](https://writing.natwelch.com/post/685), with a review of 2018 goals and a bunch of goals
    for 2019.
-   Julia Evans has an [annual review](https://jvns.ca/blog/2018/12/23/2018--year-in-review/) with a bunch of "conclusions" listing what
    worked in 2018.
-   James Clear answers [three questions every year](https://jamesclear.com/2018-annual-review) - what went well, what didn't,
    and what were the learnings.
-   [Sacha Chua](http://sachachua.com/blog/2018/08/turning-35-life-as-a-34-year-old/)'s reviews were one of the earliest reviews that I read, and they
    inspired so much awe! I may not be able to do as much quantified-self type
    posts as her, any time soon, but I love them!
-   Buster Benson does annual reviews on his [birthday every year](https://medium.com/@buster/42-dig-deeper-e2278d1fe015). He gives himself
    a motto to live-by, each year.

My review isn't as systematic as any of these. But, I have some inspiring
examples in front of me to aspire to. Hope this will start something that I can
keep doing annually from now, if not more frequently.

I've divided my review into a few different areas - based mostly the time I have
spent on them, how important I feel they are, and the extent of notes I have in
those areas.


## Work {#work}

-   I continue to work on [RSR](https://github.com/akvo/akvo-rsr/) at [Akvo](https://akvo.org/).

-   The most challenging project was to wrangle a legacy permissions system that
    worked at an organization level to give some kind of user level permissions.
    The project was plagued with incomplete communication of requirements from our
    partners, failure to understand the complexity of the legacy code, and weird
    bugs manifesting in even weirder ways. We eventually delivered something, but
    I'm not at all happy with the solution, how long it took and how the whole
    project felt.

-   The company has been in a cost-cutting mode, and has been rethinking the way
    the products are positioned - [transitioning more into a single
    solution/experience for our partners](https://akvo.org/blog/reflecting-learning-and-connecting-in-2019/). This makes a lot of sense -- the focus
    shifts from building tools to solving problems, which is great! But, I wasn't
    particularly happy about how much RSR features in these conversations. Towards
    the end of the year, our team has managed to get more conversations going on
    involving RSR, but we need more.

-   A couple of friends asked me if I'd want to work for their companies, but I
    decided not to. But, these were opportunities to think more about what I want
    out of my job and the work I do. This is a work in progress.

-   I did some mentoring at one friend's company, and got to know the team and
    their work pretty well.

-   I gave an interview at a company that I came across at PyCon which went
    horribly, partially because I didn't prepare well and partially because of
    interview jitters. I was expecting a better interview experience from them,
    though, given how much I liked their team culture, etc.

-   I also happened to take my first ever front-end interviews, along with a team
    mate. I really liked how he led the interviews, and made the interview
    candidates feel comfortable. I learned a thing or two, including the fact that
    I don't know a lot of things that people with a more structured and systematic
    approach to learning front-end development would know.

-   I didn't attend too many events this year, like always. But, I really enjoyed
    PyCon - especially the Keynotes by [Sidu Ponnappa](https://www.youtube.com/watch?v=ls1jva653bc) and [Armin Ronacher](https://www.youtube.com/watch?v=-4fzFKihmJw).


## Side projects {#side-projects}

I worked on a bunch of side-projects this year, some of them abandoned, some
completed and found useful, some abandoned after the first version turned out to
be not so useful. Most of the stuff was "webby", and unsurprisingly a bunch of
my side-projects were Ultimate related.

Zulip
: I spent a quite a bit of my spare time between about March and
    September contributing to [Zulip](https://zulipchat.com/) -- mainly as a mentor on the
    [zulip-terminal](https://github.com/zulip/zulip-terminal) project, apart from some minor contributions around
    improving setting up of the dev environment for the [zulip-server](https://github.com/zulip/zulip-terminal)
    project. I also facilitated a [Zulip sprint](https://in.pycon.org/cfp/devsprint-2018/proposals/zulip-sprint~eXlAe/) during PyCon at Hyderabad.

    I also got to attend the Zulip India Summit! It was great to meet a
    whole bunch of Zulip contributors. I especially enjoyed the
    conversations with and the presentations by Tim and Greg, mostly
    around developer productivity.

    I'm really impressed and inspired by the amount of care and effort
    that is put into stream-lining the process of contributing to the
    project, and the emphasis on developer productivity.

    I played around with a little bit of React Native development, but
    wasn't able to devote much time to it. I'd like to play around some
    more with it, this year.


Find Playo Venue
: I wrote a [simple map based tool](https://punchagan.github.io/playo-find-venue/) to find the most suitably
    located Playo venue with good ratings, when some of my friends and I were
    playing a lot of badminton together. I still use it sometimes, but we've
    mostly figured out our "favorite" venues.


moditweetarchive
: I built a [site](http://moditweetarchive.herokuapp.com/) inspired by [this Trump tweet archive](http://trumptwitterarchive.com/) for
    Modi's tweets. I used [Dash](https://plot.ly/products/dash/) to build it, and it was quite fun, despite a few
    annoyances. This tweet archive, though, isn't as interesting as the Trump
    archive, since the tweets are more calculated and strategic. But, a few
    things could be added to make it more useful.

    The repo is private as of now, but I'm happy to share the code, if anyone
    is interested.


Blaggregator
: I spent a couple of weekends maintaining [Blaggregator](https://blaggregator.recurse.com/about/). I
    updated Django to 1.11.x which is also something I did on Akvo
    RSR (my work project), later during the year. I also worked on
    making the crawl faster by handling dead blogs better, etc.


weblogviz
: I tried to get started with learning some [Rust](https://www.rust-lang.org/), and as an
    exercise, I started building a [tool to analyze Apache logs](https://github.com/punchagan/weblogviz) and
    show some useful stats.


Org-mode to Zulip helpers
: I wrote some [Emacs helpers to post to Zulip](https://github.com/punchagan/zulip-helpers.el). I'm
    quite happy with being able to post longer messages from inside Emacs -
    this lets me retain a copy of things like my checkins or interesting links
    in my notes/journal file.


aradhana.org
: I tried to help a friend of mine build a newer website for
    [aradhana.org](http://www.aradhana.org/), and spent about a couple of days on it. But,
    there were other bigger problems which needed attention from
    my friends, and this site just fell by the wayside.


Abandoned projects
: There are bunch of other projects that I've abandoned. I
    may end up spending some time looking into them, this year.


### Ultimate related projects {#ultimate-related-projects}

SOTG Calculator
: I had the chance to look at the [Spirit scoring sheets](http://www.wfdf.org/sotg/spirit-rules-a-scoring) for a
    couple of tournaments, in the beginning of 2018, and was utterly
    disappointed. I always knew that it was a lot of work to get the top scores
    just a few minutes after the final game, but I found a lot more mistakes
    than I expected -- a lot of them were easy to avoid with just a little
    automation.

    To help improve the situation, I built a [simple webapp](http://sotg-calculator.herokuapp.com/) to compute the
    scores from a Google Spread Sheet. Finding the initial adopters turned out
    to be very hard, despite the app making life a lot easier for people. It
    was disappointing to see people saying they didn't have enough time to try
    the app, and instead chose to manually compute everything that the app
    could've done with a couple of clicks!

    But, eventually it started to be pushed as the official tool starting this
    season, and has found a bunch of happy users.


Team RSVP
: We used Whatsapp to co-ordinate team practices and to keep track
    of the players attending, etc. But, this started to get quite
    spammy, and it was a hassle to have other conversations on the
    group, while folks were calling in for a practice. It was a
    nightmare to have people call in for two different events at the
    same time.

    To see if people were willing to switch away to something less
    spammy, a friend and I started with a [simple RSVP app](https://github.com/thatte-idli-kaal-soup/rsvpapp) and most
    people seemed to not mind using it.

    Unsurprisingly, the app eventually got [a lot of features](https://rsvp.thatteidlikaalsoup.team/features) - to
    make it easy to manage team practices and team resources like
    photos and training material. It is being used regularly by the
    team, without too many problems.

    As an after thought, may be we have an over-engineered solution,
    and just asking everyone to use (Google) Calender & Email
    would've worked.


Huddle magazine archive
: The Huddle was a good Ultimate related magazine run
    by Ben & Andy a few years ago. They eventually stopped running it, and the
    archives disappeared from the [original site](https://the-huddle.org/) but are available on the [USA
    Ultimate website](https://www.usaultimate.org/huddle/issue001.aspx) which is super hard to read! I wrote some [code](https://github.com/thatte-idli-kaal-soup/the-huddle) to scrape
    the site, and convert the articles into markdown posts and made a more
    readable version of the magazine [here](https://thatte-idli-kaal-soup.github.io/the-huddle/).

    I tried to get in touch with Ben & Andy, to ask if they were interested to
    replace the "coming soon" message on the original site with these archives,
    but didn't succeed. Posting it on Reddit and sharing it with my team got
    some people interested, and hopefully they keep using it.


vquiz
: To help my team with understanding rules better, I built a light
    weight [tool to easily create video based quizzes](https://github.com/punchagan/vquiz) - embed video and
    ask related questions, use videos to show answers.

    To build a question bank, I tried to get some people on the team to
    volunteer, but it didn't really take off.


## Ultimate Frisbee {#ultimate-frisbee}

2018 was filled with a lot of Ultimate - not just playing, but also thinking,
talking and planning.

-   Our team had a couple of the best tournaments that we've since I've been
    playing with the team - not just in terms of the results but in how much fun
    we all seemed to have together.

-   I captained the team in a bunch of tournaments. I'm not sure how exactly I got
    to be the captain -- I guess it was just stepping forward for a tournament and
    offering to spend the time and effort required. It was a great learning for
    me, and I've learned some things about people and leading them that I would've
    taken much longer to learn. I also think I did get better over the course of
    the year -- I got more confident and the team also trusted me much more.

-   In the past, game time at tournaments has been a big concern. We experimented
    with a bunch of simple rotation systems -- essentially just systems to keep
    track of how much each person has been playing, and trying to prevent too many
    imbalances. People were encouraged to bring forth their concerns and ideas
    during the games, rather than keep everything until the end of the tournament
    when it is not fixable until the next time!

    We had the luxury of being able to try this since everyone on the team had
    more or less the same skill level, and everyone trusted the system. It helped
    take players' minds off playing time, and helped them focus on actually making
    the most of the opportunities on the field. Most of the complaints about
    game-time seem to have gone away.

-   Communicating the reasoning behind a decision is as important as communicating
    the plan. Often, I'd hear surprising responses to a plan or just generally
    disappointing comments like how decisions were being made arbitrarily, when we
    were actually spending a lot of time and energy to try and make decisions. On
    most occasions, I felt the reason was the lack of an understanding of the
    reasons behind a decision.

-   Team communication was another tricky thing that I've had to wrestle with. The
    team still needs to find a balance between communicating over a WhatsApp group
    or discussing things in person, and the fact that most people are very busy to
    make in-person meetings with a good attendance happen. We are experimenting
    with a few things to see what works and what doesn't.

-   At tournaments, having a positive environment where everyone is supportive and
    has each others' back is the most important thing for me. Irrespective of how
    much practice we had together and what kind of strategies we practiced, just
    having a team where everyone is positive and helpful goes a long way.

    On the other hand, this positivity is also such a fragile thing that needs to
    be carefully protected and nurtured. It's very easy for one negative comment
    or thought to spread negativity and discontent like wild-fire.

    I think as a captain, I should've strived harder to safe guarding and
    cultivating this positivity in the team.

-   Thanks to some discussions I had with my teammates, I spent a lot of time
    thinking about what it means to feel like a valued member of a team, and what
    it means to feel like you are contributing and making a difference. Being
    chosen an MVP during a game is external validation that you made a difference
    in a game, but only one or two people get that validation in each game. What
    about the rest of the dozen or so other people? How can we as a team recognize
    and acknowledge each others' contributions to each point or game?

Some of these questions will continue to take up some of my mindspace this year,
whether or not I continue to captain the team.

-   I also took up the role of UPAI's [Director of Technology](http://indiaultimate.org/governance-committee) (aka sys-admin) along
    with AK. It's mostly been minor email or slack related change requests, and
    nothing more. But, it's been fun to get to know some of the people in the
    Ultimate community a little better. I also helped organize the [UPAI conference](http://indiaultimate.org/p/proceedings-of-upai-national-conference-2018).


## Writing {#writing}

-   I wrote only 8 blog posts, but 6 of them in the second half of the year!

-   Some friends and I started a [Writing Club](https://sasha.wtf/writing-club/) in July, and it's been going strong
    so far. It has not only helped me publish at least one blog post a month, but
    based on the responses I've received, I feel it has also improved the quality
    of my writing. A lot of credit goes to my friends who read initial drafts of
    my writing, and gave me really good suggestions on how to improve them.

-   My journaling and personal note taking improved slightly as compared to last
    year - I have more notes for 2018, than 2017. And that's how I was able to
    write this review post. But, I think the notes are restricted to a few areas
    of my life, and I can take some actions to write about other things that are
    important too.


## Relationships {#relationships}

-   I started a couple of Zulip instances with my friends on it -- one with my
    college friends and another with my Ultimate team mates on it. My friends from
    college went back to WhatsApp, but the other Zulip realm has had some pretty
    conversations, especially on #beanbags. It hasn't been super active towards
    the end of the year, but I'm really happy it exists, and hope it continues to
    grow this year.

-   It was good to have some more teammates turn into friends. Thanks to all the
    Ultimate stuff I've been doing, I got to spend a lot more time with some of
    the people that I previously hadn't interacted much with.

-   Tarle, a teammate and friend, passed away. 4 months and he's still dead. We
    all miss him a lot! But, we've also come together stronger, in some ways.

-   I've tried scheduling regular check-ins with some friends who live far away.
    They worked for a bit, but seem to be easily swallowed by higher priority
    things. When they did happen, though, they were quite nice!

-   Towards the end of the year, I moved houses. The new house is well furnished
    and has neighbors who mostly mind their business -- I had a lot of friends and
    family visiting, which has been good.


## 2019 goals/ideas {#2019-goals-ideas}

I want to give having a motto for an year a shot, a la Buster Benson. My motto
for 2019 is "Be Deliberate".

I'm not sure I know exactly what this entails, and I'm sure I'll get a better
understanding of it, as the year goes by. But, here are few things that I think
would be good starting points:

-   Choose what I read more deliberately, and read for understanding rather than
    just information. Keep better notes of the books I read.

-   Go back to using [Howdy](https://github.com/punchagan/howdy) or creating check-ins with more people, and making sure
    that they happen. Prefer meeting in person or audio/video calls, rather than
    chat.

-   Journal more about feelings and thoughts, especially when making decisions,
    rather than just about events. Journal about more areas of my life rather than
    just "work" related stuff.

-   Consider hiring an editor to help write better blog posts, and improve writing
    style. Getting reviews and suggestions from my Writing Club friends has been
    good, but this would be a level up.

-   Look for mentors in other areas of life - especially those where I feel like
    I'm plateauing.

-   Pick side projects more carefully. One thing that I would be deliberately
    thinking more about would be working on side projects that pay.

-   Write quarterly posts to document my improved understanding of the theme -- Be
    Deliberate -- and to track progress I'm making on these goals.

---

Thanks [Kartik Krovvidi](https://twitter.com/Kar_tiktok) and [Shantanu Choudhary](http://baali.muse-amuse.in/) for reading drafts of this post,
being excited about it, and useful suggestions to make it better.
