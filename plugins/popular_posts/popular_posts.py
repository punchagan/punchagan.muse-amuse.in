# -*- coding: utf-8 -*-

# Copyright © 2016 Puneeth Chaganti, Roberto Alsina and others.

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
""" Command to make a new post from captured bookmarks/quotes. """

from __future__ import unicode_literals, print_function

import json
from os import path

from nikola.plugin_categories import Command


def _get_popular_posts(count, site, data):
    data_path = path.join(site.config['CACHE_FOLDER'], 'popular-posts.json')
    if not site.file_exists(data_path):
        return ''

    with open(data_path) as f:
        permalinks = json.load(f)
    posts = {p.permalink(): p for p in site.posts}
    popular_posts = [posts[link] for link in permalinks]
    context = {'posts': popular_posts, 'lang': site.default_lang, 'count': count}
    return site.shortcode_registry['post-list'](site=site, **context)


class CommandPopularPosts(Command):
    """Command to create a list of popular posts."""

    name = "popular_posts"
    doc_usage = "[options]"
    doc_purpose = "Command to create a list of popular posts."
    cmd_options = [
        {
            'name': 'all',
            'long': 'all',
            'default': False,
            'type': bool,
            'help': 'Share all tags'
        },
        {
            'name': 'tag',
            'long': 'tag',
            'default': '',
            'type': str,
            'help': 'Tag to fetch, for sharing.'
        },
        {
            'name': 'dry-run',
            'long': 'dry-run',
            'short': 'n',
            'default': False,
            'type': bool,
            'help': 'Dry run.'
        },
        {
            'name': 'no-deploy',
            'long': 'no-deploy',
            'default': False,
            'type': bool,
            'help': 'Run nikola deploy.'
        }
    ]

    def set_site(self, site):
        """Set site, which is a Nikola instance."""
        super(CommandPopularPosts, self).set_site(site)
        self.site.register_shortcode('popular-posts', _get_popular_posts)

    def _execute(self, options, args):
        """Create a json file with popular posts."""

        raise NotImplementedError
