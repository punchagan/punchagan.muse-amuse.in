---
title: "Instagram's user-friendliness"
description: "TL; DR: I'm a video content creator on Instagram, and don't tell me Instagram is user friendly. Being able to preview posts before making them viewable for everyone will go a long way, though."
date: 2020-06-24T20:13:00+05:30
tags: ["blag", "rant", "tools", "software"]
draft: false
---

TL; DR: I'm a video content creator on Instagram, and don't tell me Instagram is
user friendly. Being able to preview posts before making them viewable for
everyone will go a long way, though.


## Introduction {#introduction}

I've been using Instagram quite regularly from around the beginning of this
year, posting about one video a week on an average. Previously, I used it
primarily as a content consumer for about an year, before getting off it for
quite long since it started to turn into a big time-suck. In the current stint
of using Instagram as a content-creator, I've had quite a few frustrating user
experiences. On a platform that comes with a giant reputation of being
user-friendly, this is a surprise.

A lot of my posts this year have been video content. While posting them, I ran
into a bunch of things that didn't "just work". For instance, in the first 3 or
4 posts of the [Humans of TIKS](https://www.instagram.com/tiks_ultimate/channel/) series, every post had some thing broken, leading
to a poor viewing experience.

Some of my friends, though, found it surprising that I was frustrated with
Instagram. "Isn't it very user-friendly?", I was asked by many. I think
Instagram is just riding on their reputation from the past. The newer features,
especially around video content, aren't exactly "user-friendly". Instagram does
focus on giving the content consumer a nice (read: addictive) experience. But,
as a creator, there are a bunch of hoops to jump. Content creators probably put
up with it just for the reach Instagram gives.

In this post, I've listed down everything that I see as broken. I've also tried
to suggest improvements to each broken feature that would make the experience
more friendly. I start with the more common problem scenarios and progress
towards the edge cases.


## Caption formatting is needlessly hard {#caption-formatting-is-needlessly-hard}

I've always had to fiddle with the caption of a post, after publishing it, if it
had multiple paragraphs. There's a magic algorithm that Instagram uses to decide
if multiple line-breaks in the text actually mean separate paragraphs or not.

After some trial and error, I've figured out a few things about it. For
instance, leaving a trailing space at the end of a paragraph causes paragraphs
to be joined together. But, when the second "paragraph" starts with a non-text
character, it doesn't seem to matter what the previous paragraph ends with, they
always are joined together as a single one.

I don't want to find out these details by trial and error. Adding previews for
captions would make this so much nicer. Some documentation for the "magic" would
probably help too. Instagram could even look at WhatsApp, its messaging cousin,
for some lessons on how to make writing text easier. Switching to a more common
markup language would be a nice bonus.


## Albums are restrictive {#albums-are-restrictive}

Posting multiple images in a single post (an album) is a pain. All images are
[cropped to the same orientation](https://help.instagram.com/269314186824048) -- square, portrait or landscape.

Until a few years ago, Instagram required every image to be square. If you want
to keep things dead simple for your users, the square image restriction is as
simple as it can get. At least it's easy to understand and remember, even though
I can't post my pictures exactly the way I want.

The current same orientation restriction is worse on both fronts. I'm still left
with not being able to post my pictures exactly the way I want. But, also the
restriction is not easy to infer from the UI. I had to fiddle with the UI and my
pictures for a while, to understand that there's no way around this, and that
Instagram is actually enforcing this restriction.

I don't want to be thinking about Instagram's restrictions while clicking my
pictures. I want to take the best pictures I can, and upload them with the best
possible orientation/crop.

Instagram may have these restrictions in place to ensure the best possible
"viewing" experience. But, for the creators the user-friendly thing to do here
would be to remove these restrictions. I think, even going back to the universal
square image restriction would feel more user-friendly!


## Public profiles, really? {#public-profiles-really}

I think, a public profile should be viewable by anybody without having to login,
or having to use a specific kind of device. But, Instagram's idea of "public"
profiles is quite different.

If you are not logged into Instagram, and are viewing a public profile, you are
prompted to login after scrolling down through a few posts on the profile. If
you are on a desktop browser, you can't open up any post from a public profile.
You are prompted to login, when you try to view a post. Even on a mobile
browser, you are prompted to login after opening 3 or 4 posts. Opening direct
links (or opening posts in a new tab) works, though.

Instagram obviously wants to grow as much as it can, and it doesn't really care
about people not on the platform. As a content creator, though, I care about my
audience, irrespective of whether they have an Instagram account or not. A user
friendly platform would keep their users' interests ahead of their growth goals
and not do such shady stuff. Or at least, tell us the truth and stop calling it
"public" profiles.


## So many video types! {#so-many-video-types}

When I want to post a video on Instagram, I've to first decide what kind of a
"post" to make. If I want to post a "short" video, it can go into a normal
post/album if it is under a minute. If not, I'll either need to split it up into
smaller segments, or post it as an IGTV video. Stories can only be 15 seconds
long, or they get chopped into multiple shorter stories.

IGTV supports longer videos -- from 1 minute up to 60 minutes long. The videos
need to be portrait videos with an aspect ratio of 4:5 or smaller, 9:16 is
recommended, while normal posts prefer square (1:1) videos.

Just like with pictures, I don't want to care about Instagram's restrictions
when capturing a video. I want to shoot my video, and let Instagram do what is
required to share that video. I find it strange that there are hundreds of blog
posts documenting how to upload an already recorded video to IGTV.

A user-friendly platform would let users upload the videos as they shot them,
and prompt about adding some padding, or allowing users to crop and select a
part of the video, to match the aspect ratio requirements.


## 9:16 IGTV videos are broken {#9-16-igtv-videos-are-broken}

The documented aspect ratio for an IGTV video is 9:16, but guess what! They
aren't displayed correctly in the mobile app.

{{< figure src="https://user-images.githubusercontent.com/315678/85221173-6017dc00-b3cf-11ea-8b84-43d44cf89d20.png" width="150px" >}}

They are displayed correctly in mobile and desktop browsers, though. But, given
how Instagram nudges everyone to use the app, I would guess that 90-95% of
viewers would be using the app, if not more.

{{< figure src="https://user-images.githubusercontent.com/315678/85098070-21d7bc80-b217-11ea-9432-bfb8ebe3ab0b.png" width="150px" >}}

After a lot of trial and error, I figured out that I need to upload my videos at
a ratio of 9:21 or lower to be able to prevent the sides from being chopped off.
Instagram's UI or docs don't mention this at all. Also, this workaround only
works when uploading from a destkop browser. I haven't yet figured out how to
prevent mobile uploads from looking broken.

For a visual platform that is so bullish on everything looking perfect, this is
horrendous! I don't know where to place this - is this a bug in Instagram's
processing pipeline? Or is this a part of attempts to provide the best viewing
experience? Just display my videos as advertised, please!


## Video post-processing is magic {#video-post-processing-is-magic}

Any video I upload goes through a processing pipeline, that is undocumented,
before it gets displayed to the users. This is possibly done to optimize for
space, etc., but it has led to broken user experience for at least a couple of
my videos.

On one occassion, it made the audio and video go out of sync. To be fair, the
video did have some issues with the audio stream data missing for the first 3
seconds of the video, due to a [bug in my video processing pipeline](https://github.com/thatte-idli-kaal-soup/humans/commit/77f10800ce6663e1e118b425421662206e3f50c4). The same
video worked perfectly fine in [MPlayer](http://www.mplayerhq.hu/design7/news.html), [mpv](https://mpv.io/), [VLC](https://www.videolan.org/vlc/), and on YouTube. Noticing that
Instagram's post-processing made the audio and video go out of sync, after about
50 people watched it, is such a shame!

To avoid such problems, we decided to make a demo account and upload every video
there, before posting it from the real account. Needing to do this seems super
broken to me. I still did it, since I wanted everything to work just right. But,
that wasn't to be.

We had a video where we added some background music on the video, and it ended
up having a 4-channel audio stream. It turns out the Instagram app on iOS won't
play such videos, and we only detected that after some people in our audience
let us know. Instagram has this documented on their IGTV documentation under
[additional technical details](https://help.instagram.com/1038071743007909). But, I only read that because things weren't
working. Again, our followers had a broken experience because of this.

It can be hard to "document" all the technical details of the post-processing
pipeline. But, it should be fairly easy to detect things like 4-channel audio,
and warning users about it!

Even simpler, but user-friendlier thing to do here would be to allow users to
view the video after it has been uploaded and processed, before making it
viewable by everyone. Currently, draft posts cannot be shared with friends. I'm
not sure if they can even be found and viewed from multiple devices -- it wasn't
intuitive to do this, when I tried. Just making it easy to preview posts before
sharing it publicly would make things a lot lot more user-friendly. It feels
quite backward to be using a private account for this to ensure no broken
content is published.

This may sound too extreme, but just give me the exact [ffmpeg](https://www.ffmpeg.org/) command being run
on the uploaded videos somewhere in the docs! I would then be able to verify
that my videos are Instagram compliant, without having to upload a dozen videos
and checking on multiple devices. With a lot of big brands using Instagram, I
think there'd be other "expert" users who would appreciate these details.


## Published content is uneditable {#published-content-is-uneditable}

I would find the brokenness more tolerable if I could go back and change the
uploaded videos. But, Instagram doesn't let you edit published posts. It does
seem like a reasonable restriction, since this content may have been referenced
elsewhere. This seems to be Twitter's take too, for instance.

For something as "heavy" as a video, though, it seems a little too restrictive.
It may not be a great idea to allow changing content behind people's backs. But,
I'm not happy about my followers having to watch a broken post. Deleting a
broken post and making a new one doesn't really cut it -- it feels spammy.

I'd like to see some kind of versioning added to the videos. Let user upload a
newer version, and make it possible for users to see older versions too, if they
chose to. Google Drive and Dropbox seem to do this, for instance.


## Outro {#outro}

Instagram started off by allowing users to only post square pictures. It was
very easy to undestand and use, even if not very accomodating of different use
cases. Everyone and their dog could use it!

A whole bunch of new features have been added in the last few years, trying to
compete with the other platforms. Doing the simplest thing - posting a single
picture - may still be easy to do, but trying to do anything more than that
leads to a frustrating experience quite often. I think the reputation of being
user-friendly is now just a vestige of the past.

People who use it regularly get used to its quirks and probably put up with the
annoyances, because it gives them a way to reach their audiences with whom
Instagram is popular. Instagram is "friendly" to the content consumer, and tries
its best to keep the content extremely consumable to keep them coming back for
more. The burden of figuring out and making the content fit the restrictions is
left on the content-creators. This can often be frustrating.

<div style="font-size:small;" class="reviewers">

Thanks to [Kartik](https://balu.muse-amuse.in/), Meghana, Nitin, Pratiksha, [Ranjan](https://a-travelers-tales.blogspot.com/), [Ritesh](https://www.lightstalking.com/author/riteshsaini/), [Shantanu](http://baali.muse-amuse.in) and [Vivek](https://vkrishnaswam.github.io/)
for reading drafts (or parts) of this post and helping by boucing off ideas.

</div>
