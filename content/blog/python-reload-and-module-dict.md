---
title : "Python reload and module dict"
date : "2016-06-23T00:00:00+05:30"
tags : ["blag", "python"]
draft : false
---

I was trying to play around with Nikola's code today and learnt about a
documented weirdness of Python's reload.

-   Below are two versions of code -- `ORIGINAL` and `UPDATED` respectively
    referring to the orginial code and the code after changes. The code only has a
    `PLUGINS` list, which is changed in each version of the code.

    ```python
    # Work in a temporary directory
    import os
    import tempfile
    os.chdir(tempfile.mkdtemp())

    # Module content, original and updated
    ORIGINAL = "# PLUGINS = []"
    UPDATED = "PLUGINS = ['rss']"

    def create_conf_file(content):
        """Create a conf.py module with given content."""
        with open('conf.py', 'w') as f:
            f.write(content)
    ```

-   `conf` doesn't have a `PLUGINS` attribute in the `ORIGINAL` code.  It's been commented out!

    ```python
    create_conf_file(ORIGINAL)
    import conf
    # PLUGINS is not defined in the module, originally.
    print(conf.PLUGINS)
    ```

-   The code for `conf` has been updated, but the module doesn't yet have a
    `PLUGINS` attribute, since the new module isn't imported until we reload.

    ```python
    create_conf_file(UPDATED)
    import conf
    print(conf.PLUGINS)
    ```

-   `PLUGINS` has the expected value, after the reload

    ```python
    import importlib
    importlib.reload(conf)
    print(conf.PLUGINS)
    ```

-   What happens when we revert to the `ORIGINAL` code, and reload the module?

    ```python
    # We write back the original file. PLUGINS should be empty!
    create_conf_file(ORIGINAL)
    import conf
    importlib.reload(conf)
    print(conf.PLUGINS, "<---Whaaaat!")
    ```

The behavior is well documented, along with a reasoning of why it is the way it
is, but you can trip over it if you don't know. I hit a bug and was wondering
if there was a race condition somewhere, until I read the docs for [reload](https://docs.python.org/3/library/importlib.html#importlib.reload). On
reload, **the module dict is updated**, instead of creating a new dict. Any
values **not redefined** in the new code for the module **remain unchanged**.
