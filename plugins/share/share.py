# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Puneeth Chaganti, Roberto Alsina and others.

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

import codecs
import datetime
from nikola.plugin_categories import Command
from nikola.plugins.command.new_post import get_default_compiler


ENTRY_FORMAT = """\
- %(title)s

  %(content)s
"""


def get_entries(tag):
    """ Get the entries, given the tag to fetch. """

    from os.path import exists

    base_path = '/home/punchagan/.life-in-plain-text'
    infile = '%s/%s.org' % (base_path, tag)

    if not exists(infile):
        print('No data to share.')
        entries = []

    else:
        with codecs.open(infile, encoding='utf-8') as f:
            text = f.read().splitlines()
            start = [i for i, line in enumerate(text) if line.startswith(u'- ')]
            end = [i for i in start[1:]] + [len(text)]
            entries = []

            for i, _ in enumerate(start):
                entry = text[start[i]:end[i]]
                title = entry[0].replace('-', ' ').strip()
                content = '\n'.join(entry[1:]).strip()
                entries.append(dict(title=title, content=content))

    return entries


def success(tag):
    """ Records a success of the share, to archive this capture data. """

    import shutil

    base_path = '/home/punchagan/.life-in-plain-text'
    infile = '%s/%s.org' % (base_path, tag)
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    bkfile = '%s-%s.bk' % (infile, date)
    print('Backing up capture file to', bkfile)
    shutil.move(infile, bkfile)


def new_post(tag, entries, site):
    """ Make a new post with the given entries. """

    post_format = get_default_compiler(
        True, site.config['COMPILERS'],  site.config['post_pages']
    )
    title = '%s [%s]' % (
        tag.capitalize(), datetime.datetime.now().strftime('%Y-%m-%d')
    )

    from blinker import signal

    def write_content(_, **kwargs):
        post_file = kwargs['path']
        with codecs.open(post_file, encoding='utf8') as f:
            text = [
                line.strip() for line in f.readlines()
                if not line.startswith('Write your post')
            ]
        text += [ENTRY_FORMAT % entry for entry in entries]

        with codecs.open(post_file, 'w', encoding='utf8') as f:
            f.write('\n'.join(text))

    signal('new_post').connect(write_content)

    site.commands['new_post'].execute({
        'title': title,
        'tags': tag,
        'onefile': True,
        'twofile': False,
        'post_format': post_format,
        'schedule': None,
    })

    success(tag)


class CommandShare(Command):
    """ Command to make a new post from captured bookmarks/quotes. """

    name = "share"
    doc_usage = "[options]"
    doc_purpose = "Command to make a new post from captured bookmarks/quotes."
    cmd_options = [
        {
            'name': 'tag',
            'long': 'tag',
            'default': '',
            'type': str,
            'help': 'Tag to fetch, for sharing.'
        }
    ]

    def _execute(self, options, args):
        """ Create new post and share captured bookmarks/quotes. """

        if len(options['tag']) == 0:
            tag = self.site.config.get('DEFAULT_SHARE_TAG', 'bookmarks')
        else:
            tag = options['tag']

        entries = get_entries(tag)

        if len(entries) >= self.site.config.get('SHARE_ENTRY_COUNT', 5):
            new_post(tag, entries, self.site)
        else:
            print('Only {} entries available'.format(len(entries)))

