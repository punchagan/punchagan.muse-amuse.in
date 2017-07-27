+++
title = "Jabber message queue"
date = "2014-12-10T00:00:00+05:30"
tags = ["emacs", "hack"]
draft = false
+++

I've always wanted to be able to queue up messages to send to friends, until I
go online the next time.  I tried using email instead of chat a few times, or
just ended up staying online with a busy status.

Finally, now that I have started using jabber-mode for chatting from within
Emacs, I took out the time to write a "queuing system" for sending chat
messages, similar to the mail queue for smtpmail.  Instead of persisting sexps,
though, I persist the messages in a JSON format and the queue is flushed every
time I connect to jabber, in a `jabber-post-connect-hook`.

To make the interface as similar to the interface available when I am online, I
hacked completion for the to ID using email addresses in my address book
(`mu4e~contact-list`).  I really like the fact that the chat buffer opens up,
and I can type and send messages like I usually do.  Hitting `RET` after typing
a message queues it up, instead of trying to send it. Smooth!

The code is in my [.emacs](https://github.com/punchagan/dot-emacs/blob/master/punchagan.org#jabber)
