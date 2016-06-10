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

from collections import Counter
from datetime import datetime
import gzip
import json
from os import path
import re

from nikola.plugin_categories import Command

# Regex for the Apache common log format.
PARTS = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+?)\]',                # time %t
    r'"(?P<request>.*)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referrer>.*)"',              # referrer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]
PATTERN = re.compile(r'\s+'.join(PARTS)+r'\s*\Z')
UA_FILTERS = ['bot', 'ning', 'crawler', 'spider', 'scoutjet', 'linkchecker']
UA_FILTER_PATTERN = re.compile('|'.join(UA_FILTERS), re.IGNORECASE)

# Change Apache log items into Python types.
def pythonized(d):
    # Clean up the request.
    d["request"] = d["request"].split()[1]

    # Some dashes become None.
    for k in ("user", "referrer", "agent"):
        if d[k] == "-":
            d[k] = None

    # The size dash becomes 0.
    if d["size"] == "-":
        d["size"] = 0

    else:
        d["size"] = int(d["size"])

    # Convert the timestamp into a datetime object. Accept the server's time
    # zone.
    time, zone = d["time"].split()
    d["time"] = datetime.strptime(time, "%d/%b/%Y:%H:%M:%S")

    return d

def is_post(hit):
    """Is this hit a post?"""

    hit = hit or {}
    request = hit.get('request') or ''

    return (
        request.startswith('/posts/') and
        request.endswith('.html') and
        not request.endswith('index.html')
    )

def get_hit(line):
    m = PATTERN.match(line)
    hit = pythonized(m.groupdict()) if m is not None else None
    return hit if is_post(hit) else None


def get_post_hits(logfile):
    print('Processing {}'.format(logfile))
    open_fn = gzip.open if logfile.endswith('.gz') else open
    with open_fn(logfile) as f:
        hits = [get_hit(line) for line in f]

    bad_agent = lambda x: not UA_FILTER_PATTERN.search(x['agent'] or '')
    return list(filter(bad_agent, filter(None, hits)))


def group_hits_by_week(post_hits):
    hits_by_week = {}
    for post in post_hits:
        request = post['request']
        week = post['time'].strftime('%Y-%U')
        post_counts = hits_by_week.setdefault(request, {})
        post_counts.setdefault(week, 0)
        post_counts[week] += 1

    return hits_by_week

THIS_WEEK = datetime.now().strftime('%Y-%U')

def get_weeks(start, end):
    start_year, start_week = map(int, start.split('-'))
    end_year, end_week = map(int, end.split('-'))

    if start_year == end_year:
        weeks = [
            '{}-{:02}'.format(end_year, i)
            for i in range(start_week, end_week+1)
        ]

    else:
        weeks = []
        for year in range(start_year, end_year+1):
            if year == start_year:
                start_ = start
                end_ = datetime(year, 12, 31).strftime('%Y-%U')
            elif year == end_year:
                start_ = datetime(year, 1, 1).strftime('%Y-%U')
                end_ = end
            else:
                start_ = datetime(year, 1, 1).strftime('%Y-%U')
                end_ = datetime(year, 12, 31).strftime('%Y-%U')

            weeks.extend(get_weeks(start_, end_))

    return weeks


def get_top_posts(logfiles, n=5):
    post_hits = []
    for logfile in logfiles:
        post_hits.extend(get_post_hits(logfile))

    hits_by_week = group_hits_by_week(post_hits)

    # Ignore hits in the first few weeks.
    score = lambda (x, y), i: y if i >= 4 else 0

    def average_score(counts):
        weeks = get_weeks(min(counts), THIS_WEEK)
        n = len(weeks)
        weeks = dict(zip(weeks, [0]*n))
        weeks.update(counts)
        return sum(map(score, sorted(weeks.items()), range(0, n)))/float(n)

    weekly_average_hits = {
        request: average_score(weekly_hits)
        for request, weekly_hits in hits_by_week.items()
    }

    weekly_average_hits = Counter(weekly_average_hits)
    return weekly_average_hits.most_common(n)

def write_output(top_posts):
    with open('top-posts.json', 'w') as f:
        posts = [post for post, _ in top_posts]
        json.dump(posts, f, indent=2)

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

    ]

    def set_site(self, site):
        """Set site, which is a Nikola instance."""
        super(CommandPopularPosts, self).set_site(site)
        self.site.register_shortcode('popular-posts', _get_popular_posts)

    def _execute(self, options, args):
        """Create a json file with popular posts."""

        raise NotImplementedError
        logfiles = glob.glob(path)
        top_posts = get_top_posts(logfiles, 20)
        write_output(top_posts)
