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

import jinja2
from nikola.plugin_categories import ConfigPlugin

TEMPLATE = """
<section class="wrap container comments">
    <p style="text-align: center; font-size: 60%; margin: 10px; background: #F5F5DC; padding: 10px; border-radius: 5px;">
        If you would like to comment on something I've said here, <a href="mailto:punchagan+blog@muse-amuse.in?subject=Comment on {{title|e}}">send
        me an email</a> or get in touch with me on <a class="twitter-share-button" href="https://twitter.com/intent/tweet?text={{title|e}} is interesting, /cc: @punchagan&url={{ post.permalink(absolute=True) }}">twitter</a>.
    </p>
</section>
"""

env = jinja2.Environment()
template = env.from_string(TEMPLATE)

def generate_html_bit(site, context):
    if 'post' not in context:
        return ''

    post = context['post']
    if not context['enable_comments'] or post.meta('nocomments'):
        return ''

    return template.render(**context)

class MyComments(ConfigPlugin):
    """ Insert a mailto line for comments. """

    name = "comments"

    def set_site(self, site):
        """Set site, which is a Nikola instance."""
        super(MyComments, self).set_site(site)
        # Hack to get comments above everything else...
        items = site.template_hooks['body_end']._items
        items.insert(0, (True, generate_html_bit, True, (), {}))
