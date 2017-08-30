---
title : "OAuth2 demystified"
date : 2014-06-20T10:09:51-04:00
tags : ["hackerschool", "oauth2"]
draft : false
---

## Motivation {#motivation}

I was trying to pair on writing a simple app that uses Hacker
School's OAuth2 API, and hit a roadblock on the first step of
requesting an authorization from the user.  Once the user authorized
my app, I would see an error that said, "The authorization server
does not support this response type".  I was using a client library
that I had [used before](https://github.com/litl/rauth), and the server was using a what seemed like
a [popular implementation](https://github.com/doorkeeper-gem/doorkeeper) for ruby on rails.  Getting weird errors is
not done!

I have used OAuth2 based authentication [before](https://github.com/punchagan/statiki/blob/master/statiki.py#L49), but the thought of
using it always makes me a little nervous, just because

1.  I don't understand it very well.
2.  Like almost everything else, there seem to be so many libraries
    for doing this in Python, and I'm never sure which one to use, or
    which one I used the last time around.  Not understanding the
    protocol also doesn't let me debug anything that comes up.

To fix this, I set about to read and understand the [OAuth2 protocol](http://tools.ietf.org/html/rfc6749).
This blog post is an attempt to record it for future reference, and
possibly act as a reference for others.


## Why OAuth {#why-oauth}

OAuth is simply a way for an end-user to allow third parties to use
protected data, without sharing the user's credentials with the
third-party.

For example, an end-user (Jane) can grant a printing service
(Printo) access to her protected photos stored at a photo-sharing
service (Picasa), without sharing her username and password with the
printing service.  Instead, she authenticates directly with a server
trusted by the photo-sharing service, which issues the printing
service delegation-specific credentials. (example from the OAuth 2.0
spec)


## Protocol Flow {#protocol-flow}

The flow occurs through a sequence of user actions, client requests
and user-agent (browser) redirects.

-   (A) Printo asks Jane to allow using Picasa Data. The request can
    be sent directly to Jane, but is usually routed via
    Picasa/Google.

-   (B) Printo gets back an authorization grant, which is a
    credential representing Jane's authorization or approval.  The
    type of the actual grant credential depends on the type of
    request that Printo used.

-   (C, D) Printo gets back to Google with the credentials it obtained
    in the previous step and obtains a token that it can use to talk
    with Picasa.

-   (E, F) Printo asks for the desired photo with the token it
    obtained previously, and Picasa gives back the photo to print.
    Jane gets her framed photo!

But before any of this happens, the client needs to register with
the authorization server and obtain a `client_id` and
`client_secret`, that will be used to identify the client making
the requests.


## Pythonized "authorization code" work-flow. {#pythonized-authorization-code-work-flow-dot}

The OAuth2 spec allows the authorization request/grant to be of 4
different types.  It also allows some flexibility in the token
type.

In my experience, the most common work-flow seems to be using an
_authorization code_ as an authorization grant, and using a _Bearer_
type token.  This work-flow is explained in the diagram below (taken
from the spec document).  This diagram zooms in, onto the steps A-D
in the diagram above.

This [python code snippet](https://gist.github.com/punchagan/76e8771fc26cd243f3ac) is a simple implementation of this
workflow, using the Hacker School API.

<script src="https://gist.github.com/76e8771fc26cd243f3ac.js"></script>


## Conclusion {#conclusion}

I think, I understand the OAuth2 spec a lot better now, and hope
that this will help others understand it, too.  And more
importantly, I won't get nervous when I have to add it to my
projects.

Also, [oauthlib](https://github.com/idan/oauthlib) for Python seems to be a pretty thorough
implementation of the spec, and [requests-oauthlib](https://github.com/requests/requests-oauthlib) seems to wrap it
for use with requests.  I think I'm going to use this in my future
projects.
