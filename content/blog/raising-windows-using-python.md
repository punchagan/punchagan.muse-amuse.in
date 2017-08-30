---
title : "Raising Windows using Python"
date : "2010-11-03T00:00:00+05:30"
tags : ["python"]
draft : false
---

Posting a small snippet of code, that I've been using for months
now, on the request of a friend [^fn:1].

It basically checks for open windows of a program and brings them
to the foreground or starts the program. I use it for my 3 most
commonly used programs --- Emacs(Mod4+E), Firefox(Mod4+F) and the
Terminal(Mod4+T). I'm using a neat tool called xdotool [^fn:2] to
search for windows using titles.

-   <kbd>Mod4+E</kbd> is mapped to `~/bin/raise.py emacs`

Similarly, for firefox and terminal.

```python
#!/usr/bin/env python
import subprocess
import sys

if len(sys.argv) < 2:
    print "Usage %s window-name" %(sys.argv[0])
    exit(1)

program = sys.argv[1]

# Having different variables helps, in case of some programs.
window = program

# search for windows titled "window"
search = subprocess.Popen("xdotool search --class %s" %(window),
                          stdout=subprocess.PIPE, shell="FALSE")
search_output = search.stdout.readlines()
search.stdout.close()
print search_output

search_output = [each.strip() for each in search_output]

# Raise the first window or start the program
if len(search_output) is not 0:
    subprocess.Popen("xdotool windowactivate %s"
                     %(search_output[0]), shell="FALSE")
else:
    subprocess.Popen(program, shell="FALSE")

```

Feel free to use it as you like. :)

Any improvements and suggestions are welcome.

[^fn:1]: dusual on twitter
[^fn:2]: xdotool - Homepage
