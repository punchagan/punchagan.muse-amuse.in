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
import subprocess

from blinker import signal

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
                title = entry[0].replace('-', ' ', 1).strip()
                content = '\n'.join(entry[1:]).rstrip()
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

    subprocess.check_call([
        'emacsclient',
        '--eval',
        '(when (get-buffer "bookmarks.org") (kill-buffer "%s.org"))' % tag
    ])



def run_deploy():
    """ Run the nikola deploy command. """

    subprocess.check_call(['nikola', 'deploy'])


def new_post(tag, entries, site, dry_run=False):
    """ Make a new post with the given entries. """

    content_format = get_default_compiler(
        True, site.config['COMPILERS'],  site.config['post_pages']
    )
    title = '%s [%s]' % (
        tag.capitalize(), datetime.datetime.now().strftime('%Y-%m-%d')
    )

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

    if dry_run:
        [print(entry['title']) for entry in entries]

    else:
        signal('new_post').connect(write_content)

        site.commands.new_post(**{
            'title': title,
            'tags': tag,
            'onefile': True,
            'twofile': False,
            'content_format': content_format,
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

    def _execute(self, options, args):
        """ Create new post and share captured bookmarks/quotes. """

        if options['all']:
            tags = self.site.config.get('SHARE_TAGS', ['bookmarks', 'quotes'])
        elif len(options['tag']) == 0:
            tag = self.site.config.get('DEFAULT_SHARE_TAG', 'bookmarks')
            tags = [tag]
        else:
            tag = options['tag']
            tags = [tag]

        created = [self._share_tag(tag, options['dry-run']) for tag in tags]

        if any(created) and not options['no-deploy']:
            run_deploy()

    def _share_tag(self, tag, dry_run=False):
        """ Create a Share post for the given tag. """

        self.site.scan_posts()

        entries = get_entries(tag)

        if len(entries) >= self.site.config.get('SHARE_ENTRY_COUNT', 5):
            new_post(tag, entries, self.site, dry_run)
            created = True

        else:
            print('Only {} entries available'.format(len(entries)))
            created = False

        return created
