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

import re

import jinja2
from nikola.plugin_categories import Task
from nikola.utils import config_changed
import numpy as np
from scipy.spatial.distance import cdist
from sklearn.feature_extraction.text import TfidfVectorizer


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


def compute_related_posts(site, count=5):
    """Compute and set related_posts attribute for all the posts."""

    vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english', use_idf=True)
    posts = [p for p in site.timeline if p.use_in_feeds]
    post_texts = [
        '{} {}'.format(post.title(), post.text(strip_html=True).lower())
        for post in posts
    ]
    vectors = vectorizer.fit_transform(post_texts).toarray()
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
