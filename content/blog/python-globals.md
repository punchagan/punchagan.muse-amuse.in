---
title: "Python's globals"
date: 2018-07-25T21:11:00+05:30
tags: ["python", "tests", "programming", "blag"]
draft: false
---

## TL; DR {#tl-dr}

-   The `global` statement is a parser directive to indicate that `globals` are
    being used. When looking up `globals`, the `globals` of the current scope are
    fetched.

-   Python's `globals` are really just module-level.

-   Every function has an associated `__globals__` dictionary, which is the **same
    as the module's `__dict__` for the module where it was defined**. This
    `__globals__` dict is the name-space that is looked up when trying to fetch
    `globals` within a function.

-   Avoid globals to make it easier to test functions


## Motivation {#motivation}

During a mentoring session I was doing recently, we ran into a problem with
`globals` in Python.

Here is a toy example to describe what we were seeing.

We had code in a module `foo.py` where the function `f` was using a global
defined in `main`, and we were trying to write tests for the function `f`.

```python
# foo.py
def f():
    print(a)


def main():
    global a
    a = 5
    f()

if __name__ == '__main__':
    main()
```

Running this file `foo.py` prints out `5` as expected.

We would now like to import `f` into a different module and use it.


## Running `f` in a different module {#running-f-in-a-different-module}

```python
# bar.py
from foo import f

def main():
    f()

main()
```

Running the module `bar.py` gives us a `NameError`, as expected. The name `a`
was defined in the `main` in `foo.py` which is never being run when the code is
imported in `bar.py`

```python
Traceback (most recent call last):
  File "bar.py", line 10, in <module>
    main()
  File "bar.py", line 7, in main
    f()
  File "foo.py", line 5, in f
    print(a)
NameError: global name 'a' is not defined
```


## Setting a global value for `a` {#setting-a-global-value-for-a}

We'd like to be able to run `f` without running `main` and the first fix that
comes to mind is to set the value of `a` in `bar`, and let `f` use that.

```python
# bar.py
def main():
    global a
    a = 4
    f()
```

Surprise! Nothing changes.

```python
Traceback (most recent call last):
  File "/tmp/example/bar.py", line 13, in <module>
    main()
  File "/tmp/example/bar.py", line 9, in main
    f()
  File "/tmp/example/foo.py", line 5, in f
    print(a)
NameError: global name 'a' is not defined
```

Why doesn't this work?!


## Function `__globals__` and the `global` statement {#function-globals-and-the-global-statement}

The `global` statement is a directive to the parser, that specifies that the
variable being assigned to is a global variable.

This can be seen by looking at the disassembled code for `f`

```python
import dis
from foo import f

dis.dis(f)
```

```asm
5           0 LOAD_GLOBAL              0 (print)
            2 LOAD_GLOBAL              1 (a)
            4 CALL_FUNCTION            1
            6 POP_TOP
            8 LOAD_CONST               0 (None)
           10 RETURN_VALUE
```

`globals` for the current frame are fetched, and the value is updated in that
dict. Each function in Python has an associated `__globals__` dict which is a
reference to that module's `__dict__` in which the function was defined. So, in
the case where we try to set the `a = 4` in `bar.main`, the `main` function's
`__globals__` dict is being updated.

```python
# bar.py
def main():
    global a
    a = 4
    print(main.__globals__.keys())
    print(main.__globals__['a'])
```

```python
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'foo', 'f', 'dis', 'main', 'a'])
4
```

As you can see `a` is being set to `4`, but `f` still doesn't see value, since
it has it's own `__globals__` dictionary. Printing the `globals` dictionary for
`f` should make that clear.

```python
from foo import f
print(f.__globals__)
```

If the variable `a` was declared in the module `foo` outside of any of the
functions, it would be in `f`'s `__globals__` dict when it is imported, and
hence the name error would go away, but setting it still would not work.

```python
# foo.py
a = 3

def f():
    print(a)


def main():
    global a
    a = 5
    f()

if __name__ == '__main__':
    main()
```

```python
# bar.py
from foo import f

def main():
    global a
    a = 4
    f()

main()
```

Running `bar.py` would print the value `3` which has been defined in `foo.py`,
and not `4`.


## Updating `__globals__` {#updating-globals}

To update the value of `a` for `f`, we could modify it's `globals` dict.

```python
# bar.py
from foo import f

def main():
    f.__globals__['a'] = 4
    f()

main()
```


## Module `__dict__` and monkey-patching {#module-dict-and-monkey-patching}

As mentioned previously, a function's `__globals__` dict is a reference to the
module's `__dict__` for the module where the function was defined. So, we could
achieve the same result as above by updating `foo.__dict__`. And setting an
attribute on the module `foo` is the same as updating this dict.

```python
# bar.py
import foo
from foo import f


def main():
    foo.a = 4
    f()
```

If you have used a library like `mock` to patch some code while running tests,
this is essentially what is happening. The `target` module's dict is looked up
for the specified object/function and replaced with a mock object.


## Use an argument to make it testable {#use-an-argument-to-make-it-testable}

The function `f` would've been much easier to test, if it took `a` as an
argument, instead of using a global value. This functional approach would make
the code easier to reason about too.

```python
# foo.py
def f(a):
    print(a)


def main():
    a = 5
    f(a)

if __name__ == '__main__':
    main()
```

```python
# bar.py
from foo import f

def main():
    a = 3
    f(a)
```
