+++
title = "Recurse Center, 2014-07-24"
date = 2014-07-24T09:53:03-04:00
tags = ["python", "raspberry_pi"]
categories = ["recursecenter"]
draft = false
+++

## Glowing LEDs and me {#glowing-leds-and-me}

-   It turned out that the SPI driver exposed a faster way to write bits, writing
    to all the LEDs at once, instead of one at a time, and this was sufficient to
    get things working!

-   Kyle and I started to have enough, of the glowing LEDs and decided to wrap up
    the project, but, Nick had different ideas for us! We had talked about having
    the music stream via airplay, but Nick got his DJing tools, and it would be
    too bad to not use it for the party, but doing that meant Airplay's delay
    wouldn't help the DJ. So, we connected a line-in, and thought we'd be done if
    we just read the input and used that data. But, it turns out that's not so
    simple because sending data over the wire, added noise to it, and in a whole
    range of frequencies! I tried removing all the fourier coefficients which
    were lower than a threshold, but I felt like it didn't work very well, until
    Nick reduced the gain of this output on the amp to the very minimum. Finally,
    Kyle and I decided that this was good enough for the party!

-   I also hacked up a quick script to read a font file, and use the grey values
    to get ascii characters to show up on the LED strip.


## Miscellaneous {#miscellaneous}

-   While trying to find the RPi on the network, I learnt that `sudo nmap -sP
      10.0.1.*` gives us the hostname as well, instead of just IPs.  `sudo` being
    the key, here.

-   Kyle and I went and grabbed dinner in a restaurant in west village. It was
    good to sit down and talk about various things, and eat. The glowing LEDs
    were totally out of my mind for that period, and the break was good!

-   There were a bunch of HSers doing mock-interviews and it was fun to watch, so
    I stayed on until quite late, when all of us headed out together.


## Today {#today}

-   I'm excited about trying to build a small version control system from
    scratch today!

-   Though I have had quite a bit of glowing LEDs in my face for the past week,
    I may suck up to it, and figure out how to do scrolling text on the
    display.

-   Also, excited to see how all the cool projects will come together in the
    party tonight!
