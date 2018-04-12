---
title : "Weird ISP Issue"
description : "At the end of my debugging skills for a weird network issue"
date : 2018-04-12T11:09:00+05:30
tags : ["blag", "networking", "debugging"]
draft : false
---

I was trying to lookup the documentation for [Click](http://click.pocoo.org/5/) and I got redirected to a
page showing Werkzeug's documentation. I'd assumed it was a broken configuration
on the server, because other subdomains like [Armin's blog](http://lucumr.pocoo.org) also sent me to the
same page. I [got in touch with Armin](https://twitter.com/punchagan/status/983885853343727616) and he asked me if I was using [https
everywhere](https://www.eff.org/https-everywhere), and that wasn't supported by the server. But, I wasn't. The next
thing to try was to switch my ISP and check, and viola it worked!

I did some debugging and figured out that in some responses the HTTP status line
was not being sent, and the first line in the response contained `Date`. Also,
the response seems to be correct, when I hit a hard refresh on the browser,
which sets the `Cache-Control` header to `no-cache`. So, it looks like some
cache in between me and the server is going nuts with this specific request.

```sh
$ nc click.pocoo.org 80 < input.txt
Date: Thu, 12 Apr 2018 05:17:14 GMT
Last-Modified: Mon, 07 Apr 2014 18:35:36 GMT
Connection: Keep-Alive
```

And the `input.txt` file looks like this.

```text
HEAD / HTTP/1.1
Host: click.pocoo.org
User-Agent: Mozilla/6.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/59.0
Accept: */*
Accept-Encoding: deflate, gzip

```

Adding the line `Cache-Control: no-cache` to this input causes the problem to go
away.

```sh
$ nc click.pocoo.org 80 < input.txt
HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Thu, 12 Apr 2018 05:30:56 GMT
Content-Type: text/html
Content-Length: 178
Connection: keep-alive
Location: http://sphinx-doc.org/
```

Also, I'm able to reproduce this with all the subdomains on `pocoo.org` -
`click`, `sphinx`, `lucumr`, ... I'm not sure if it has something to do with the
server, or if it is entirely independent of that. But, the problem does go away
when I switch to a different network.

I'm not sure what I can do next to narrow down the problem, even more. Any
hints/tips appreciated.
