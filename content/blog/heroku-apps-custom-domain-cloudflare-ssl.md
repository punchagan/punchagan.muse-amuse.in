---
title: "Heroku apps with custom-domain and Cloudflare SSL"
description: "Setup a flask app on Heroku with https for a custom domain using Cloudflare"
date: 2019-03-14T13:03:00+05:30
tags: ["programming", "blag", "heroku", "https", "security"]
draft: false
---

## Motivation {#motivation}

I have a bunch of small (toy?) apps hosted on Heroku. They are probably used by
a few dozen people, at most. For these apps, I'd like the following setup:

1.  Use a custom domain for the apps
    -   Heroku provides domains of the form `appname.herokuapp.com` for all apps.

    -   But, it also has the option to add one or more custom domains

    -   I usually already have a domain under which I want to add a sub-domain,
        where these apps would run.

2.  Use HTTPS for all connections
    -   The domains or the sub-domains usually don't already already have an SSL
        certificate. With lets-encrypt, I guess this can change in future.

    -   Heroku provides SSL certificates for the default domain
        (`appname.herokuapp.com`) for free.

    -   They also have an option to buy SSL certificates for custom domains, but
        they are expensive!

    -   I'm going to use [Cloudflare's free SSL service](https://www.cloudflare.com/ssl/) instead. I'd like to have
        SSL for the full domain, and not just the app's subdomain.

3.  Redirect all the requests to the Heroku domain to the custom domain
    -   Nobody should really be using the `appname.herokuapp.com` domain, in case
        I'd like to move away from it.

    -   A few lines of app (Flask) code can do this for us.


## Setup {#setup}


### Setup DNS to use Cloudflare {#setup-dns-to-use-cloudflare}

Since we plan to use Cloudflare for the SSL certificates, we need to change DNS
settings at our domain registrar to use Cloudflare. We first need to create a
Cloudflare account, and [let Cloudflare do a DNS scan](https://support.cloudflare.com/hc/en-us/articles/201720164-Step-2-Create-a-Cloudflare-account-and-add-a-website) to add all the existing
domain settings automatically. Next we point to the [Cloudflare DNS servers](https://support.cloudflare.com/hc/en-us/articles/205195708) on
our domain registrar.


### Enable HTTPS always in Cloudflare {#enable-https-always-in-cloudflare}

Using [page rules in Cloudflare](https://support.cloudflare.com/hc/en-us/articles/218411427#always-use-https), add a rule for the whole domain to "Always use
HTTPS". For example, use the url `http://*example.com/*` and select the `Always
use HTTPS` option.


### Select the SSL option to use {#select-the-ssl-option-to-use}

Cloudflare provides [different options for the SSL setting](https://support.cloudflare.com/hc/en-us/articles/200170416-What-do-the-SSL-options-mean-) which changes whether
or not traffic is encrypted between Cloudflare and the Heroku app.

Choose `Full (strict)` to enable encryption between Cloudflare and Heroku.

If you are not so concerned about encryption between Cloudflare and Heroku, you
could select the `Flexible` option too.


### Add a custom domain in Heroku {#add-a-custom-domain-in-heroku}

Add a [custom domain](https://devcenter.heroku.com/articles/custom-domains) -- `app.example.com` -- in Heroku's settings.

Heroku provides a DNS Target that needs to be used as the destination for a
CNAME setting in the DNS provider (Cloudflare). The DNS Target looks something
like `foo-bar-123abcdef.herokudns.com`

If you chose `Full (strict)` SSL option, this DNS target cannot be used and can
be ignored.


### Add a CNAME for the subdomain {#add-a-cname-for-the-subdomain}

[Add a new CNAME setting](https://support.cloudflare.com/hc/en-us/articles/360019093151-#h%5F60566325041543261564371) in Cloudflare for `app.example.com` and use the
app's Heroku domain name (`appname.herokuapp.com`) as the destination value/IP
address.

It is important to use the `appname.herokuapp.com` value if the SSL settings you
chose above was `Full (strict)`. Using the DNS Target provided by Heroku instead
(`foo-bar-123abcdef.herokudns.com`) would give an [SSL Handshake error](https://support.cloudflare.com/hc/en-us/articles/200278659) since the
SSL certificate provided by Heroku only works for the `appname.herokuapp.com`
domain, and not for `foo-bar-123abcdef.herokudns.com`.

If you chose `Flexible`, though, you can use the DNS Target provided by Heroku
-- `foo-bar-123abcdef.herokudns.com`.

Also, ensure that the Cloudflare Proxy Toggle is toggled on -- _the cloud icon
is orange, not grey_!


### Redirect all requests {#redirect-all-requests}

We redirect all the requests coming to the old domain to the new one.

```python
@app.before_request
def redirect_heroku():
    """Redirect herokuapp requests."""
    urlparts = urlparse(request.url)
    if urlparts.netloc == "appname.herokuapp.com":
        urlparts_list = list(urlparts)
        urlparts_list[1] = "app.example.com"
        return redirect(urlunparse(urlparts_list), code=301)
```


## Enforce HTTPS on Heroku {#enforce-https-on-heroku}

If you don't care about a custom domain and just wish to enforce SSL for the
Heroku domain (`appname.herokuapp.com`), `Flask-SSLify` is the way to go. The
app can be hosted on Heroku and we can use the certs provided for free.

```python
from flask_sslify import SSLify
app = Flask(__name__)
if "DYNO" in os.environ:
    # Always use SSL if the app is running on Heroku (not locally)
    sslify = SSLify(app)
```


## Conclusion {#conclusion}

I've done this setup, or some parts of it quite a few times, but each time I
seem to need to look up the documentation. Every time, it seems to take longer
than it needs to! Hopefully, this post will make it quick and reproducible.
