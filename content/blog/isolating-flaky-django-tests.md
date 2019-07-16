---
title: "Isolating flaky Django tests"
description: "Couple of django tricks to isolate flaky Django tests"
date: 2019-06-05T18:37:00+05:30
tags: ["python", "django", "tests", "blag"]
draft: false
---

The Zulip repository had a bunch of flaky tests that were fixed a few weeks ago.
I learnt a couple of tricks that I wasn't aware of during this.

Django's test runner has an [option](https://docs.djangoproject.com/en/1.11/ref/django-admin/#cmdoption-test-reverse) to run tests in the reverse order. The
documentation of this option explicitly mentions that this option is useful for
debugging side-effects of tests that are not properly isolated. I wasn't aware
of this option, and it's a pretty neat tool.

The test runner also has a [`--parallel` option](https://docs.djangoproject.com/en/1.11/ref/django-admin/#cmdoption-test-parallel) to run tests in parallel, and the
Zulip server uses this option when running the back-end tests. I never really
bothered to look into how test cases are assigned to different processes. The
Django docs explain:

> Django distributes test cases — `unittest.TestCase` subclasses — to subprocesses.
> If there are fewer test cases than configured processes, Django will reduce the
> number of processes accordingly.
>
> Each process gets its own database. You must ensure that different test cases
> don’t access the same resources. For instance, test cases that touch the
> filesystem should create a temporary directory for their own use.

When running tests in parallel, the set of tests running in the same process can
vary quite a bit based on the execution speed of tests in different processes.
To add more variation to the order in that tests are run, the number of
processes being used could also be changed.

These two tools combined together can get tests to run in different orders than
the usual order in which they usually get run, and can help find tests which are
not well isolated.

It could be a good idea to run tests in parallel (with a randomly chosen,
reasonable number of processes) and with the `--reverse` flag, once in every few
CI runs, or as a cron job periodically.

---

<div style="font-size:small;" class="reviewers">
  <div></div>

Thanks to [Shantanu Choudhary](https://baali.muse-amuse.in) for nudging me to write this post, and reading
drafts of this post. Thanks also to [Tim Abbott](https://blog.zulip.org/author/tabbott/) for making me aware of these
tricks.

</div>
