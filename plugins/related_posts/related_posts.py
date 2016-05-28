# -*- coding: utf-8 -*-

# Copyright © 2016 Puneeth Chaganti and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

""" A simple plugin to insert mailto line for comments. """

import codecs
from collections import Counter
import functools
import math
import re

import jinja2
from nikola.plugin_categories import Task
from nikola.utils import config_changed
import numpy as np
from scipy.spatial.distance import cdist


TEMPLATE = """
<section class="related wrap container content">
<h2> Related Posts </h2>
<ul class="related-posts">
{% for related_post in post.related_posts %}
<li><h3><a href="{{related_post.url}}">{{ related_post.title }}</a></h3></li>
{% endfor %}
</ul>
</section>
"""

STRIP_RE = re.compile('[^A-Za-z ]')
TOKEN_RE = re.compile(r"(?u)\b\w\w+\b")

env = jinja2.Environment()
template = env.from_string(TEMPLATE)

def generate_html_bit(site, context):
    if 'post' not in context:
        return ''

    post = context['post']
    related_posts = getattr(post, 'related_posts', [])
    if not post.is_post or not related_posts:
        return ''

    return template.render(**context)

def _get_post_text(post):
    """ Return the text for the given post. """

    with codecs.open(post.source_path, 'r', 'utf-8') as post_file:
        post_text = post_file.read().lower()
        if not post.is_two_file:
            post_text = post_text.split('\n\n', 1)[-1]
        post_text = post.title() + ' ' + post_text

    return post_text.lower()


def _get_post_words(post, use_tags=False):
    """ Return words from the text of a given post. """

    post_text = _get_post_text(post)
    # post_words = STRIP_RE.sub('', post_text).lower().split()
    post_words = TOKEN_RE.findall(post_text.lower())

    if use_tags:
        tags = set(post.tags)
        post_words = list(tags) + [word for word in post_words if word in tags]

    return post_words


def _get_post_tfs(post, use_tags=False):
    post_words = _get_post_words(post, use_tags=use_tags)
    word_counts = Counter(post_words)
    length_ = math.sqrt(sum([x*x for x in word_counts.values()]))
    tf = {word: count/length_ for word, count in word_counts.items()}
    return tf

def _get_post_tf_idf_vector(tfs, idfs, vocabulary):
    vector = [
        tfs[word] * idfs[word] if word in tfs else 0
        for word in vocabulary
    ]
    return vector


def compute_related_posts(site, count=5):
    """Compute and set related_posts attribute for all the posts."""

    posts = [p for p in site.timeline if p.use_in_feeds]
    vectors = get_tf_idf_vectors(posts)
    distances = cdist(vectors, vectors, 'cosine')
    sorted_indexes = np.argsort(distances)
    related_posts = {}

    for i, post in enumerate(posts):
        related = [
            {'title': posts[index].title(), 'url': posts[index].permalink(absolute=True),}
            for index in sorted_indexes[i][1:count+1] # nearest post would be itself
        ]
        related_posts[post.source_path] = post.related_posts = related

    site.cache.set('related_posts', related_posts)
    return related_posts


def get_tf_idf_vectors(posts, use_tags=False, stop_words=False, min_df=None, max_df=None):
    """Return a tf-idf vectors array for the given posts."""

    n = len(posts)
    post_tfs = {
        post.source_path: _get_post_tfs(post, use_tags=use_tags) for post in posts
    }

    def update_idf(idf, terms):
        # Add 1 to idf for every word in terms
        idf.update(terms.keys())
        return idf

    word_document_counts = functools.reduce(update_idf, post_tfs.values(), Counter())
    idfs = {word: math.log(n/(1+x)) for word, x in word_document_counts.items()}

    if isinstance(min_df, float):
        min_df = int(min_df*n)

    if isinstance(min_df, int):
        max_idf = math.log(n/(1+min_df))

    else:
        max_idf = math.log(n)

    if isinstance(max_df, float):
        max_df = int(max_df*n)

    if isinstance(max_df, int):
        min_idf = math.log(n/(1+max_df))

    else:
        min_idf = math.log(n/(1+n))

    idfs = {word: idf for word, idf in idfs.items() if min_idf <= idf <= max_idf}


    if stop_words:
        from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
        vocabulary = sorted(set(idfs) - ENGLISH_STOP_WORDS)

    else:
        vocabulary = sorted(idfs)


    tf_idf_vectors = [
        _get_post_tf_idf_vector(post_tfs[post.source_path], idfs, vocabulary)
        for post in posts
    ]

    return np.array(tf_idf_vectors), vocabulary


class RelatedPosts(Task):
    """Insert related posts for each post."""

    name = "related_posts"

    def set_site(self, site):
        """Set site, which is a Nikola instance."""
        super(RelatedPosts, self).set_site(site)
        site.template_hooks['body_end'].append(generate_html_bit, True)

    def gen_tasks(self):
        """Compute and populate related posts."""

        related_posts = self.site.cache.get('related_posts') or {}
        for post in self.site.timeline:
            post.related_posts = related_posts.get(post.source_path, [])

        kw = {
            'count': self.site.config.get('RELATED_POSTS_COUNT', 5),
            'cached_related_posts': len(related_posts) > 0,
        }

        yield {
            'basename': self.name,
            'actions': [(compute_related_posts, (self.site, kw['count']))],
            'task_dep': ['render_posts:timeline_changes'],
            'uptodate': [config_changed(kw)],
        }
