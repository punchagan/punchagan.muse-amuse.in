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
import operator
import re
import string

import jinja2
from nikola.plugin_categories import Task
import numpy as np
from scipy.spatial.distance import cdist


TEMPLATE = """
<section class="related-posts wrap container content">
<h3> Related Posts </h3>
<ul>
{% for related_post in post.related_posts %}
<li><a href="{{related_post.url}}">{{ related_post.title }}</a></li>
{% endfor %}
</ul>
</section>
"""

PUNCTUATION = re.compile('[{}]'.format(string.punctuation))

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
    """ Return the text of a given post. """

    with codecs.open(post.source_path, 'r', 'utf-8') as post_file:
        post_text = post_file.read().lower()
        if not post.is_two_file:
            post_text = post_text.split('\n\n', 1)[-1]
        post_text = post.title() + ' ' + post_text

    return PUNCTUATION.sub('', post_text).lower()


def _get_post_tfs(post):
    post_text = _get_post_text(post)
    word_counts = Counter(post_text.split())
    length_ = math.sqrt(sum([x*x for x in word_counts.values()]))
    tf = {word: count/length_ for word, count in word_counts.items()}
    return tf

def _get_post_tf_idf_vector(tfs, idfs, vocabulary):
    vector = [
        tfs[word] * idfs[word] if word in tfs else 0
        for word in vocabulary
    ]
    return vector


def get_related_posts(site):
    """Get related posts for all the posts."""

    posts = [p for p in site.timeline if p.use_in_feeds]
    n = len(posts)
    post_tfs = {
        post.source_path: _get_post_tfs(post) for post in posts
    }

    def update_idf(idf, terms):
        # Add 1 to idf for every word in terms
        idf.update(terms.keys())
        return idf

    word_document_counts = functools.reduce(update_idf, post_tfs.values(), Counter())
    idfs = {word: math.log(n/(1+x)) for word, x in word_document_counts.items()}
    vocabulary = sorted(idfs)

    tf_idf_vectors = {
        post:
        _get_post_tf_idf_vector(post_tfs[post.source_path], idfs, vocabulary)
        for post in posts
    }

    related_posts = {}
    posts = list(tf_idf_vectors.keys())
    vectors = np.array(list(tf_idf_vectors.values()))
    distances = cdist(vectors, vectors, 'cosine')
    sorted_indexes = np.argsort(distances)

    for i, post in enumerate(posts):
        related = [
            {'title': posts[index].title(), 'url': posts[index].permalink(absolute=True),}
            for index in sorted_indexes[i][1:6] # nearest post would be itself
        ]
        related_posts[post.source_path] = post.related_posts = related

    site.cache.set('related_posts', related_posts)


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

        yield {
            'basename': self.name,
            'actions': [(get_related_posts, (self.site,))],
            'task_dep': ['render_posts:timeline_changes'],
            'uptodate': [len(related_posts) > 0],
        }
