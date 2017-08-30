---
title : "Learning to use Org-drill"
date : 2014-10-14T00:07:04-04:00
tags : ["emacs", "learning", "orgmode", "software"]
draft : false
---

Org-drill is an Org-mode extension that provides spaced-repetition and
flash-card functionality.  It has a [wonderful documentation on Worg](http://orgmode.org/worg/org-contrib/org-drill.html), but
somehow I couldn't get myself to read the whole document, and setup org-drill,
until now.

The setup is quite straight forward, once you have org-mode along with the
`contrib` packages.  Just `(require 'org-drill)`, and you are all set!  To add
a new card, all you need to do is add a `:drill:` tag to the items you wish to
"Org-drill".  You can start a review session with simply <kbd>M-x org-drill</kbd>.  You
will be shown flash cards, and you can rate how correct and comfortable you
were, in answering the questions.  Based on your responses, the cards are
scheduled for review.  Start another review session, whenever you need one!

What I could only understand once I got myself to read the whole document was
that:

-   The default scope of a drill session is the current file.  But, you can start
    sessions with scopes like current tree, current directory, or a specified
    list of files. This is super-useful!

-   The review sessions are not automatically scheduled, based on when you
    schedule failed flash-cards.  Scheduling the review for a card only sets a
    due-date for them, and effects, what you are asked in your next session.

Cram mode and incremental reading are also things I want to try, as I go along.

Happy Learning!
