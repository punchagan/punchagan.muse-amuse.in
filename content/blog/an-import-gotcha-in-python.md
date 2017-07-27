+++
title = "An import gotcha in Python"
date = "2012-08-20T00:00:00+05:30"
tags = ["python"]
draft = false
+++

Pankaj and I were stuck with this weird bug recently.  We had
a class `A` and a subclass `B` and an instance of B, b, was
returning False for `isinstance(b, A)`.

After some debugging, we found that it was a problem with
imports, and the same module was being imported twice, using
two different names -- `bar` and `baz.bar`.

Here's a cooked-up example to demonstrate the "bug".  We
create a package baz, as shown below.

```text
$ tree baz
baz
├── bar.py
├── foo.py
└── __init__.py
```

We have our two classes, `A` and `B` defined in the `bar`
module.

```python
class A(object):
    pass

class B(A):
    pass
```

We run `foo.py` and scratch our heads for a while, before
figuring out what's wrong...

```python
# We add the directory containing out package 'baz' to sys.path to be
# able to import using the package name.
import sys
sys.path.insert(1, '/tmp')

# We import A from bar module present in the same directory as foo
from bar import A
# We import B from bar, but refer to it, as a submodule of baz
from baz.bar import B

a = A()
b = B()

print "isinstance(b, A) -->", isinstance(b, A)

for cls in (A, B):
    print "%s -->" %cls, cls

for module in sys.modules:
    if 'bar' in module:
        print module, sys.modules[module]
```

    isinstance(b, A) --> False
    <class 'bar.A'> --> <class 'bar.A'>
    <class 'baz.bar.B'> --> <class 'baz.bar.B'>
    baz.bar <module 'baz.bar' from '/tmp/baz/bar.pyc'>
    bar <module 'bar' from 'bar.pyc'>
