---
title : "Back, Hopefully"
date : "2017-09-01T22:47:00+05:30"
tags : ["blog", "blab", "writing"]
draft : false
---

I haven't written anything here for almost a year. I needed to break the
silence. So, here we go with a not-so-useful post showing how frequently I have
been posting to this blog, to get a sense of how long this break has been in
comparison to other silences in the past.

Neither the code below, nor the plots are very insightful. But, I just hope this
will get me started on the path to blogging more regularly. See you around!


## Parsed post content {#parsed-post-content}

I wrote some code to parse the content of the blog, and each post object looks
something like this:

```text
{'date': datetime.datetime(2010, 3, 17, 18, 30, tzinfo=<UTC>),
 'draft': False,
 'tags': ['blab', 'life', 'poem'],
 'title': 'Just another bunch'}
Post count: 190
```


## Post frequency by year {#post-frequency-by-year}

```ipython
import pandas
posts = pandas.DataFrame(posts)
counts = posts['date'].groupby(posts['date'].dt.year).count()
plot = counts.plot(kind='bar', figsize=(8, 6))
plot.set_xlabel('Years')
plot.set_ylabel('# of posts')
```

<matplotlib.text.Text at 0x7f7d99ee20f0>
{{<figure src="/images/ob-ipython-64158e1b9b5ccddff8534006a256c5b3.png">}}
<matplotlib.figure.Figure at 0x7f7d99ea7390>


## Post frequency by month {#post-frequency-by-month}

```ipython
# Add a DatetimeIndex to the Dataframe
posts.index = pandas.DatetimeIndex(posts['date'].values)
counts = posts['date'].groupby(pandas.TimeGrouper('M')).count()
ax = counts.plot(kind='bar', figsize=(12, 8))

n = 5
ticks = ax.xaxis.get_ticklocs()
labels = counts.index.strftime('%Y-%m')
labels = ax.xaxis.set_ticklabels(labels[::n])
ticks = ax.xaxis.set_ticks(ticks[::n])

ax.set_xlabel('year-month')
ax.set_ylabel('# of posts')
```

<matplotlib.text.Text at 0x7f7d99e2f240>
{{<figure src="/images/ob-ipython-bf5d9e24f4f23986583d3023df42c707.png">}}
<matplotlib.figure.Figure at 0x7f7d99e2cf98>


## Work-flow {#work-flow}

I jumped onto the [hugo](https://gohugo.io) bandwagon too.

I was totally impressed by how fast it is, and have been meaning to try it out
for a while, but wasn't impressed with the built-in `org-mode` support it came
with. This changed when I finally came across the [ox-hugo](https://github.com/kaushalmodi/ox-hugo) package that does a
wonderful job of exporting blog posts from an org file to hugo's markdown
format. I have contributed a couple of patches to it, to make it work better for
myself and hopefully for others too.

Also, for this post, I used `ob-ipython` with the [enhancements from scimax](http://kitchingroup.cheme.cmu.edu/blog/2017/01/29/ob-ipython-and-inline-figures-in-org-mode/) and
it has really made the whole experience quite enjoyable.

Among other things, I think one of the reasons for those peaks in the second
half of 2010, was having a smooth work-flow. My current work-flow feels pretty
nice too, and I hope it'll reduce some of the friction in writing more posts.

Onwards!
