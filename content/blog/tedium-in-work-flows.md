+++
title = "Tedium in work-flows"
date = "2016-05-19T00:00:00+05:30"
tags = ["blab", "programming", "user_experience", "workflow"]
draft = false
+++

I use [Nikola](http://getnikola.com) for generating this blog. When creating a new post, it prompts for
a title, and creates a file for the post.

Often I'm starting off with only a vague idea that needs to be fleshed out
before it can be published (or discarded). It is quite difficult to come up
with a title at this stage. I just want to start a draft and write things down!

I could use a "draft-title" and change it after finishing a post, but this
feels tedious -- requires 3 steps -- change the title, post filename and post
slug.  The last two steps are optional, really, but I feel they are important
especially when the original title is very different from the new one.

Being forced to come up with a title before anything else, feels tedious and,
adds to the effort required to start off a new post.  I shouldn't really be
worrying about the effort required to change the title of an unwritten post,
but it happens subconsciously.

To work around this, I now have a "re-title utility" in my editor that takes
care of all the tedious details.  I can start with a random title, like
Draft-1, and change it when I'm done with the post.  I feel this is going to
lead to a lot more drafts, at the very least, if not published posts.

Another work-flow related thing I came across recently was @Malabarba's [issue](https://github.com/clojure-emacs/cider/issues/1717#issue-150907043)
on CIDER (an IDE for Clojure in Emacs).  The [REPL](http://www.braveclojure.com/getting-started/#Using_the_REPL) takes a while to startup and
this caused him to not use CIDER for running tests, if there wasn't an already
open REPL.

The tedium that people feel effects how they use the tool.  Not surprisingly,
making tedious-feeling tasks a breeze with the tool also effects how and how
much they use it.  Subtle variations in a work-flow could make or break it.
How do you discover such potential work-flow make-or-break-ers? I think, these
things would help:

-   Use the tool yourself (dog-food)
-   Talk to (or watch!) people using your tool
-   Look at work-flows in other similar tools
-   Thinking explicitly about various scenarios and simplifying or improving
    work-flows

I'd love to hear examples of this, and any ideas or thoughts you may have on
identifying and fixing such things!
