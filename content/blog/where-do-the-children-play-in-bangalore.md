---
title: "Where do the Children Play (in Bangalore)"
description: "Find good Playo venues in convenient locations"
date: 2018-02-12T13:11:00+05:30
tags: ["blag", "sport", "hack"]
draft: false
images: ["images/playo-find.jpg"]
---

A bunch of us have recently started playing Badminton regularly (on weekends),
in Bangalore. We use [Playo](https://playo.co/) to book a court to play on. But, all of us live in
different parts of the city, and it's often difficult to find a convenient place
to play. Often, we end up in bad courts because we don't pay enough attention to
the ratings, while focusing on trying to find a court in a convenient location.

To help make this search easier, I built a [small web app](https://punchagan.github.io/playo-find-venue/) that shows the venues
from Playo on a map, and then allows you to specify the locations of players,
and the radius (in km) that they are willing to travel. Hopefully, we end up
finding a good court in the overlapping region. Clicking on the venue marker
allows you to jump to the Playo booking page for that venue. The source is
available [here](https://github.com/punchagan/playo-find-venue/).

{{< figure src="/images/playo-find.jpg" >}}

-   I usually go with [leaflet](http://leafletjs.com/) when I want to do map related stuff. This is the
    first time I used [Google APIs](https://developers.google.com/maps/documentation/javascript/), and it was a pretty decent experience.
-   I also ended up using the [Google URL shortener API](https://developers.google.com/url-shortener/) to make it easier to share
    URLs. The entire state of the app is being saved in the URL fragment, so that
    URLs are shareable, but it makes them long and ugly. Short URLs seemed like a
    good workaround.
-   I got most of it working with vanilla javascript, until I started doing things
    where I felt it would be nice to have a light-weight two-way data and view
    binding library. I ended up trying [knockoutjs](http://knockoutjs.com/) for the first time, and enjoyed
    using it.
-   The data for Playo venues is updated everyday using a [cron job that runs on
    Travis](https://docs.travis-ci.com/user/cron-jobs/). So, the ratings of venues should be pretty up-to-date.
-   But, Playo allows players to rate venues overall, and not by sport. So, it may
    so happen that the venue is a decent one overall, and has good facilities for
    some other sport, but the badminton courts are still bad. But, some venues are
    badminton only, and in those cases the ratings are more useful.
-   It should be pretty easy to make the app [fetch data for other things](https://github.com/punchagan/playo-find-venue/blob/68a39a1f0ed0e13f59a529fb28853bad360b95ba/js/places.js#L90) like
    restaurants/movie theaters, to make this app do more than just help find Playo
    venues.

To Moar Badminton!

<iframe width=" 700" height=" 500" src="https://www.youtube.com/embed/PiiZrZTrOFY?rel=0&amp;hd=1&amp;wmode=transparent"></iframe>
