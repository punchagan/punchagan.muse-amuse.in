---
title : "Multiple remotes with nullmailer"
description : "Configuring nullmailer with multiple remote SMTP destinations"
date : 2017-11-18T04:50:00+05:30
tags : ["emacs", "email", "hack"]
draft : false
---

This a reference for future-me, and possibly someone pulling off an all-nighter
trying to get `nullmailer` to use the correct "remote".


## What is nullmailer and why use it? {#what-is-nullmailer-and-why-use-it}

[Nullmailer](https://github.com/bruceg/nullmailer) is a simple mail transfer agent that can forward mail to a remote
mail server (or a bunch of them).

I use Emacs to send email, and it can be configured to talk to a remote SMTP
server to send email. But, this blocks Emacs until the email is sent and the
connection closed. This is annoying, and having `nullmailer` installed locally
basically lets Emacs delegate this job without blocking.


## Why multiple remotes? {#why-multiple-remotes}

I have multiple email accounts, and I'd like to use the correct remote server
for sending email based on the FROM address.

I expected `nullmailer` to have some configuration to be able to specify this.
But, it turns out that `nullmailer` just forwards the email to all the
configured remotes [until one of them succeeds](https://github.com/bruceg/nullmailer/blob/master/src/send.cc#L382-L410).


## How do we, then, send email from the correct remote SMTP server? {#how-do-we-then-send-email-from-the-correct-remote-smtp-server}

Currently, I have two remotes - my personal domain (`@muse-amuse.in`) and GMail.

Having GMail as the first remote in `nullmailer`'s configuration wouldn't let me
send emails from my personal domain. GMail seems to agree to send the email
coming from `@muse-amuse.in`, but overwrite the MAIL FROM address and change it
to my GMail address.

So, `@muse-amuse.in` has to be the first remote. But, this server also seemed to
accept and send emails with a `@gmail.com` `FROM` address. This was causing
emails sent from my GMail ID to go into spam, as expected.

I had to reconfigure this mail server to reject relaying mails that didn't
belong to the correct domain names -- i.e., reject relaying emails which had
`@gmail.com` in the `FROM` address.

`smtpd_sender_restrictions` had to modified to have `reject_sender_login_reject`
along with other values, and the `smtpd_sender_login_maps` had to be set to
allow only the `@muse-amuse.in` domain. [This serverfault answer](https://serverfault.com/questions/318334/how-to-enforce-sender-address-to-be-logged-in-userexample-org-in-postfix) explains this in
more detail.
