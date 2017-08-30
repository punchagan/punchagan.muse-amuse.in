---
title : "Recurse Center, 2014-06-24"
date : 2014-06-24T09:44:34-04:00
tags : ["crypto", "pandas"]
categories : ["recursecenter"]
draft : false
---

-   I worked for the whole day on implementing [an algorithm](http://www.tandfonline.com/doi/abs/10.1080/0161-119591883944) to analyze a
    cipher text, and guess the substitution cipher used.  The algorithm
    was pretty straight forward, and I had it "mostly" working, in a
    couple of hours.
-   I then began to refactor it, and found that there was what looked
    like a bug, and I "fixed" it mindlessly.  I was essentially trying
    to swap 2 rows, and columns of a pandas data frame.  I had a
    data-frame `D` and its copy `D_`.  I was trying to swap 2 rows and
    columns of `D_`.  I found that the code was initially using the data
    from `D` to do the swap.  To fix it, I checked if tuple unpacking
    did the right thing.  It looked like it did.  So, I used something
    like `_D['a'], D_['b'] = D_['b'], D_['a']`.  Essentially, changed `D`
    on the right hand side to `D_`.  I thought I had tested this on the
    terminal, but after hours of debugging (along with fixing another
    minor issue), I later found out that the tuple unpacking doesn't
    work and the swapped rows and columns actually become equal!  I had
    suspected this initially, and had "tested" this manually, I
    thought.  These are the kinds of things that should have tests for,
    I think.  It wouldn't have taken me too long to write a test, and I
    could have been totally sure that it works!  (I was manually reading
    off values in the array, and probably messed up somewhere)

    FWIW, the code now reads <kbd>_D['a'], D_['b'] = D_['b'].copy(),
      D_['a'].copy()</kbd>
-   The algo seems to need about 1000 characters to get past the 90%
    accuracy mark.  I could probably tweak it a little to perform
    better, but I'm going to leave it here, for now, and move on to the
    signal processing parts.  I'm not totally sure how the signal
    processing would work, and whether we could actually map back the
    keystrokes to a substitution cipher enciphered text.
-   If required, the tweaks could be -
    -   Use trigrams instead of bigrams
    -   Add a degree of dictionary look-ups: May be something like,
        look-up all the deciphered words, and try not swapping the
        characters that appear in most of the words that are in the
        dictionary.
-   This paper is 20 years old, and there would surely be work by others
    building on top of this, or doing it totally differently.
