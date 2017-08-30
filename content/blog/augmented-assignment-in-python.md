---
title : "Augmented assignment in Python"
date : "2010-10-04T00:00:00+05:30"
tags : ["note", "numpy", "ology", "python"]
draft : false
---

If you are new to `Python`, you should probably stop reading here.
But, if you have used `Python` and `numpy`, then read on. Before, that
try these bits of code.

```python
import numpy
a = numpy.array([1,2])
a = a + 0.5j
print a
```

The "same thing", in a slightly different way.

```python
import numpy
a = numpy.array([1,2])
a += 0.5j
print a
```

Both the code blocks, look really the same, until you look carefully.
Under normal circumstances <kbd>a = a + b</kbd> and <kbd>a += b</kbd> behave exactly
similarly, and we really don't need to bother about the differences
between them.

But, <kbd>+=</kbd>, which is an augmented assignment operator, actually tries
to perform the operation in-place, unlike the other statement where
`+` actually returns a new object which is again being referenced by
the name `a`.

But, when dealing with `numpy` arrays, this will lead to trouble.
When assigning to an array, it's `dtype` is not changed and hence the
trouble.

The right way to use the augmented assignment operator, would be:

```python
import numpy
a = numpy.array([1,2], dtype=complex)
a += 0.5j
print a
```

The same thing is explained in this thread.  Also, Thanks to
Bhanukiran for asking me this.
