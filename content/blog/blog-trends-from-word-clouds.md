---
title : "Blog trends from word clouds"
description : "Year wise Word clouds for my blog posts"
date : "2017-09-11T22:15:00+05:30"
tags : ["data", "visualization", "blog", "blag"]
draft : false
meta_img : "images/word-cloud-top.gif"
---

I came across a couple of fun word clouds, and felt like generating a word cloud
for my blog content to get a sense of the major themes on my blog, over the
years.

With some [simple Python code](https://github.com/punchagan/data-projects/blob/master/blog/process_data.py#L134), I was able to parse the blog and get the word
frequency over the years. I then used a [modified version](https://github.com/punchagan/data-projects/blob/master/blog/viz.js) of [this d3 example](http://bl.ocks.org/lorenzopub/820bec1dafa6a5cd11aa23c1268edcbf) to
generate a word cloud.

Using all the words used in each year to generate the word-cloud, made it very
noisy. So, I switched to using only the top 50 words for each year.

{{<figure src="/images/word-cloud-top.gif">}}

The word cloud doesn't seem very useful or insightful, but was fun to generate.
Each year's cloud seems to have some words that gives me a sense of some major
events/themes for that year, though it may not be very apparent to anybody other
than me.

The years which have a lot of posts have clear winners, but the winning words
are quite generic. For example, 2007 has words like "life", "time", etc., as
winners. To try to get rid of the generic words in the word cloud, I tried a
quick and dirty `tf-idf` based word-cloud, but it didn't really seem to help.

{{<figure src="/images/word-cloud-tfidf.gif">}}

I might get back to this later, to try and improve the `tf=idf` word cloud.
There are also other problems, like code-blocks in posts contributing variable
names, urls contributing domain names, etc.

Also, a simple line chart of the usage of tags vs. year might give a better
sense of the themes in the blog by year, even though it may not look as fancy as
a word-cloud.
