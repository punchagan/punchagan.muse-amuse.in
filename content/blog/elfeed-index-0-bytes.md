---
title: "Why my Elfeed index was 0 bytes"
description: "How I lost my Elfeed database and learnt about Emacs's write-region"
date: 2026-01-30T16:58:00+05:30
tags: ["emacs", "blag", "elfeed", "programming"]
categories: ["best"]
draft: false
---

My Linux machine crashed, while I was in the middle of a video call. I
restarted quickly, and continued the discussion. Later, when I was trying to
sync [Elfeed](https://github.com/skeeto/elfeed) updates onto the [Elfeed Offline](https://github.com/punchagan/elfeed-offline/) app on my phone, I found it acting
weird. All the [bazillion things]({{< relref "offline-friendly-elfeed-web-ui" >}}) needed to get it working were in place, but it
was still complaining about the Emacs Elfeed server not being accessible. I
tried opening Elfeed inside Emacs and failed! The index file in [Elfeed's DB was
empty]({{< relref "elfeed-db-back-up-hooks" >}})! Gone! Poof!

Frustrating, but I didn't have time to look into what happened. I would've been
furious if I had been using Elfeed for longer and had a lot more metadata
saved. But, it was only a few weeks of lost metadata - posts I read, starred,
etc. I quickly setup a [Git based backup]({{< relref "elfeed-db-back-up-hooks" >}}) to prevent future losses and moved on.

Later, I found time to dig into what might have happened...


## The breadcrumbs {#the-breadcrumbs}

Elfeed stores all the metadata for all the posts in an `index` file with a
[content addressed store](https://en.wikipedia.org/wiki/Content-addressable_storage) of the contents of each of the posts. The index file is
simply a dump of the hash-table containing the metadata for the subscribed
feeds, their entries and metadata like tags, read/unread status, etc.

The DB save happens in [`elfeed-db-save`](https://github.com/skeeto/elfeed/blob/a39fb78e34ee25dc8baea83376f929d7c128344f/elfeed-db.el#L271), which simply dumps the hash-table to
disk inside a call to the `with-temp-file` macro.

```emacs-lisp
(defun elfeed-db-save ()
  ; <snip>
  (with-temp-file (expand-file-name "index" elfeed-db-directory)
    ; ...
    (princ (format ";;; Elfeed Database Index (version %s)\n\n"
                       elfeed-db-version))
    ; ...
    (prin1 elfeed-db)
    ;...
    ))
```

`with-temp-file`, as its documentation says, lets you create a new buffer,
evaluate the `body` there, and write the buffer to `file`. For a moment, I
thought there was some temporary file involved, but nope! I guess the name
comes as an extension from `with-temp-buffer` which does create a temporary
buffer where the `body` of the macro gets evaluated. Stripped to its core, [this
function](https://github.com/emacs-mirror/emacs/blob/3b547e4f5dc99dc157b52a059cf234f7a5d15112/lisp/subr.el#L5300-L5318) is:

```emacs-lisp
`(let ((,temp-file ,file)
       (,temp-buffer (generate-new-buffer " *temp file*" t)))
   (prog1
       (with-current-buffer ,temp-buffer
         ,@body)
     (with-current-buffer ,temp-buffer
       (write-region nil nil ,temp-file nil 0))))
```


## `write-region` and `O_TRUNC` {#write-region-and-o-trunc}

So, [`write-region` is the workhorse](https://github.com/emacs-mirror/emacs/blob/3b547e4f5dc99dc157b52a059cf234f7a5d15112/src/fileio.c#L5512) which writes the contents of the temporary
buffer to disk. It's a roughly 300 line long C function that essentially opens
the file with the flags `O_WRONLY | O_CREAT | O_TRUNC` (in this case) and then
does something to write the contents to the file, etc. Honestly, I didn't look
at anything else too carefully after I spotted the `O_TRUNC`.

The man page of `open` explains `O_TRUNC` as follows:

> O_TRUNC :: If the file already exists and is a regular file and the access mode
>         allows writing (i.e., is O_RDWR or O_WRONLY) it will be truncated to
>         length 0.

Voilà!

The write is not atomic. The file first gets truncated to length 0, and then we
hope that the new contents get correctly written before something goes wrong.

It now makes sense why the file got truncated to 0 bytes. The crash happened
after the `open`, but before the write. Somehow the crash happened in this
short window, and poof!


## Emacs has backup files, doesn't it? {#emacs-has-backup-files-doesn-t-it}

Temporary files with `~` in their file extensions have definitely annoyed me in
the past when Emacs created them where I didn't want them. So, I do know that
Emacs has back-up mechanisms out of the box. But, it turns out that the backups
occur in code paths that are more interactive, like `save-buffer`,
`write-file`, etc. And not via the programmatic APIs like `write-region` or the
higher level `with-temp-file`. `save-buffer` calls `backup-buffer` before
writing, but `write-region` is much more low-level and doesn't deal with
backups.


## The fix {#the-fix}

My "fix" for this is to backup the Elfeed data in a git repository to be able
to recover from any such corruptions of data, which I already wrote about [here]({{< relref "elfeed-db-back-up-hooks" >}}).

I know that any code that uses `with-temp-file` (or `write-region`) could be
affected by this, and the right fix for this may be to write to a temporary
file and rename it. Maybe next time I lose data I'll actually fix it properly.
