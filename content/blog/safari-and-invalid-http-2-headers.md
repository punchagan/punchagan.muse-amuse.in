---
title: "Safari and invalid HTTP/2 headers"
date: 2026-01-16T21:37:00+05:30
tags: ["blag", "emacs", "ocaml", "web"]
draft: false
---

[Elfeed-offline](https://github.com/punchagan/elfeed-offline/) currently has a [Dream web server](https://camlworks.github.io/dream/) which acts as a proxy server in
front of Elfeed's Emacs [simple-httpd](https://github.com/skeeto/emacs-web-server/tree/master) server.

simple-httpd supports HTTP/1.1 protocol, while Dream provides transparent
upgrading of connections to HTTP/2 — if the client can handle HTTP/2 and the
connection is using HTTPS, it is transparently upgraded to HTTP/2.

My proxying code was too simplistic in forwarding the headers too along with
the content received from the simple-httpd server. Some of the HTTP/1 headers
are no longer valid in HTTP/2. And, Safari (and curl) strictly adhere to the
protocol and fail if there are invalid headers. Curl, for instance, fails with
the following error:

```text
< HTTP/2 200
< server: simple-httpd (Emacs 30.1)
< date: Fri, 16 Jan 2026 10:57:25 GMT
* Invalid HTTP header field was received: frame type: 1, stream: 1, name: [connection], value: [keep-alive]
* [HTTP2] [1] received invalid frame: FRAME[HEADERS, len=77, hend=1, eos=0], error -531: Invalid HTTP header field was received
* HTTP/2 stream 1 was not closed cleanly: unknown (err 4294966765)
* Connection #0 to host 192.168.1.5 left intact
curl: (92) Invalid HTTP header field was received: frame type: 1, stream: 1, name: [connection], value: [keep-alive]
```

This was causing issues for [@Feyorsh](https://github.com/Feyorsh) who was trying out elfeed-offline with
Safari. Thanks for taking the time to debug the problem and for suggesting a
fix!
