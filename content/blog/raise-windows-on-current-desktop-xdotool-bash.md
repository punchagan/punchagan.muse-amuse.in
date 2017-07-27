+++
title = "Raise windows (on current desktop) xdotool & bash"
date = "2010-11-06T00:00:00+05:30"
tags = ["code", "hack"]
draft = false
+++

I posted a snippet [^fn:1] of python code that used xdotool to
raise windows.  I got one patch from dusual [^fn:2] that
enabled raising of windows in the current workspace only.

More importantly, Jordan gave a one-liner [^fn:3] in bash,
that could do the same thing as my long and elaborate python
snippet.  I had a feeling that this would be much shorter in bash,
but I don't feel comfortable writing bash scripts. :P

Below is a bash snippet that tries to incorporates both the
changes. :)

```sh
found=0

for win in `xdotool search --class $1`;
do
if [ `xdotool get_desktop_for_window $win` -eq `xdotool get_desktop` ];
then found=1; break;
fi;
done

if [ $found -eq 1 ]; then xdotool windowactivate $win; else $1; fi
```

**Note**: When you've visual effects enabled (the default option on
Ubuntu), getting the current desktop/workspace doesn't work,
probably because Root Window properties are being messed around by
it.

**Note2**: `search` takes an option `--screen`. It'd be nice if it
 also had an option `--desktop`.  This task could then be done in
 a one-liner.

[^fn:1]: My python snippet
[^fn:2]: dusual on twitter
[^fn:3]: Jordan's one liner
