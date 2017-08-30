---
title : "cStringIO and unicode"
date : "2012-12-03T00:00:00+05:30"
tags : ["bug", "note", "python"]
draft : false
---

StringIO in the cStringIO module in Python 2.7.2 doesn't handle
unicode strings properly.  This bug has bitten me on a couple of
occasions, in the recent past.

Just making a note for myself:

1.  Use StringIO if speed doesn't matter so much.
2.  Whenever possible, just convert the input to StringIO to a
    string, if what you are doing doesn't really require unicode
    strings.

Or may be it's just time to move up to Python 2.7.3
