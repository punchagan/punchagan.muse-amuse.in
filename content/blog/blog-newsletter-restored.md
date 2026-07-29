---
title: "Blog Newsletter Restored"
description: "Mailchimp deleted my blog's newsletter account declaring it \"inactive\". I restored it using a new Hugo template, GitHub actions and Resend."
date: 2026-07-27T16:42:00+05:30
tags: ["blog", "newsletter", "hack", "email", "blag"]
draft: false
---

I had a newsletter for this blog automatically created from the RSS feed and
sent by Mailchimp, based on [Julia Evans' setup](https://jvns.ca/blog/2017/12/28/making-a-weekly-newsletter/). I discovered this week, thanks
to Ringo, that sign-ups no longer worked. Upon digging further, I found out
that my Mailchimp account was deleted over an year ago. I missed a handful of
email reminders from them to login to the account to prevent deletion.

I didn't need to tweak or change anything with the newsletter on Mailchimp once
everything was satisfactorily set-up. For a service that provides an automatic
service, asking users to login to prove that the account is active is a dark
pattern that's more than just "mildly inconvenient". Emails are easy to miss or
get lost "in transit" given how they work. Relying on users taking action in
response to emails before deleting their data is horrid. But I guess I
shouldn't expect much more for a service I wasn't paying for.

<aside>

This reminds me of an annoying feature of Indian banks -- they want customers
to [re-KYC](https://web.archive.org/web/20260606172158/https://rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=3782) (see Q22) every year. If I'm using a bank account regularly, I don't
really understand why they want an update of my details every year -- even
things like my father's name, etc., which won't change periodically. 🤷

</aside>

The newsletter had about 25-30 subscribers, if I remember correctly, the last
time I checked maybe ~3 years ago. It's not a lot, but I definitely have had
some people writing to me that they enjoyed some editions! I've restored the
newsletter functionality using a hack-ish setup, now, thanks to Claude Code.

I've signed up to [Resend](https://resend.com/broadcasts) for sending out the newsletter. I considered using my
own mailserver to send out these emails, but I know email service providers are
usually not happy with bulk email coming out from servers/domains without
enough "[reputation](https://web.archive.org/web/20260706182426/https://www.twilio.com/en-us/blog/insights/5-ways-check-sending-reputation)" behind them.

To prevent any future data loss ala Mailchimp, I've used "[the baali trick](https://baali.muse-amuse.in/posts/collecting-user-feedback.html)"
(term coined by Claude Code) for setting up the sign-up form using a Google
Form that write responses to a spreadsheet that gets synced to Resend's
subscriber list. Unsubscribe is automatically handled by Resend and the data
about who unsubscribed is not synced back to the spreadsheet. Thi is the only
thing I'd be losing if a mailchimp like mishap occured again.

An important difference in how the newsletter gets generated is that the
current workflow doesn't depend on the RSS feed. Instead, I use a custom Hugo
[template](https://github.com/punchagan/punchagan.muse-amuse.in/blob/b6383d16b0f507b872cbdc6560377d76efbe0823/layouts/partials/newsletter-body.html) that helps to [generate](https://github.com/punchagan/punchagan.muse-amuse.in/blob/b6383d16b0f507b872cbdc6560377d76efbe0823/scripts/newsletter-send.py) the HTML email containing all the posts written
since the last send. The newsletter gets sent out every Thursday, using a
[GitHub action](https://github.com/punchagan/punchagan.muse-amuse.in/blob/b6383d16b0f507b872cbdc6560377d76efbe0823/.github/workflows/newsletter.yml).

I wonder if I should automatically add the details of those I knew subscribed
previously (but may have unsubscribed), or ask them if they'd like to be
"re-subscribed". If you'd like to receive (at the most) weekly emails from me,
containing posts from this blog, you can sign up [here](https://punchagan.muse-amuse.in/subscribe/).
