---
title : "Better styling bookmarklet"
date : "2016-06-07T00:00:00+05:30"
tags : ["blag", "hack", "web"]
draft : false
---

Some sites that I like a lot for their content, have zero styling on them.
I find it pretty hard to read when the lines are long and I have to read all
the way on my screen.

I had a simple bookmarklet until now that just changed the width of the page.

```js
document.getElementsByTagName('body')[0].setAttribute('style', 'width: 600px')
```

[Kamal](https://twitter.com/kamalx) shared with me [a recommendation](http://bettermotherfuckingwebsite.com) for 7 simple styling rules that will make
pages easier to read. I liked them, and modified my bookmarklet to use these
rules now.

{{<figure src="../images/better-websites.gif">}}

Drag and drop the link below onto your bookmarks bar if you want to use it.

<p><a style="border: 0.05em dashed; padding: 0.5em;" href='javascript:void(function(){style = document.createElement("style"); document.head.appendChild(style); style.sheet.insertRule("body{ margin:40px auto; max-width:650px; line-height:1.6; font-size:18px; color:#444; padding:0 10px; }"); style.sheet.insertRule("h1,h2,h3{ line-height:1.2 }")}())'>Better website</a></p>

The code in a readable format is below.

```js
// Create new stylesheet

(function() {
    // Create the <style> tag
    var style = document.createElement("style");

    // Add the <style> element to the page
    document.head.appendChild(style);

    // Add rules from bettermotherfuckingwebsite.com
    var sheet = style.sheet;
    sheet.insertRule("body{ margin:40px auto; max-width:650px; line-height:1.6; font-size:18px; color:#444; padding:0 10px; }");
    sheet.insertRule("h1,h2,h3{ line-height:1.2 }");

})();
```

**Update <span class="timestamp-wrapper"><span class="timestamp">[2016-06-07 Tue]</span></span>**: [baali](https://twitter.com/baali_) pointed me to Firefox's [Reader View](https://support.mozilla.org/en-US/kb/firefox-reader-view-clutter-free-web-pages) which works well too.
