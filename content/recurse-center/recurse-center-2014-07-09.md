---
title : "Recurse Center, 2014-07-09"
date : 2014-07-10T10:21:45-04:00
tags : ["python", "unicode"]
categories : ["recursecenter"]
draft : false
---

-   Unicode issues: it turned out that (atleast) one of the files had a character
    that wasn't UTF-8 encoded. I got around it by trying 'utf-8', if not falling
    back to 'iso-8859-1'.  Now that I think about it, I should fallback to
    'utf-8' with replace, if that doesn't work either.
-   I did a little clean up on the way the indexes were stored, to be able to
    have a `getfile`, to mimic `inspect`'s API.
-   I also "improved" the IPython startup script to monkey-patch the source code
    formatter/colorizer to not break with C modules.
-   The one-on-one with Allison was pretty useful, and I feel a little more
    relaxed now.
-   I paired with Kyle to get streaming audio working for his OSX app.  It
    doesn't work yet, but we made progress! Hope to get it working today.
-   I spent the late evening trying to refactor some of the code and clean it up.
-   Also, updating the py-clang code to the latest version fixed the issue of
    unknown cursor kinds.
-   I may present my project in today's presentations!
