var hide_all_quotes = function(quotes) {
    for (i=0; i<quotes.length; i++) {
        quotes[i].hidden = true;
    }
}

var show_all_quotes = function(event) {
    if (event) {
        event.preventDefault();
    }
    window.location.hash = '';
    var quotes = document.querySelectorAll('.quotes .org-ul li');
    for (i=0; i<quotes.length; i++) {
        var q = quotes[i];
        q.hidden = false;
        q.style.listStyleType = '';


        if (!q.querySelector('.permalink')) {
            var link = document.createElement("a");
            link.setAttribute('href', window.location.pathname + '#' + i);
            link.setAttribute('class', 'permalink');
            link.setAttribute('onclick', 'show_random_quote(null,'+i+')');
            link.textContent = "#";
            q.appendChild(link);
        }
    }
}

var show_random_quote = function(event, i) {

    if (event) {
        event.preventDefault();
    }

    var quotes = document.querySelectorAll('.quotes .org-ul li');
    hide_all_quotes(quotes);

    var index;

    if (i!=undefined) {
        index = i;
    } else {
        try {
            index = Number(location.hash.match("#(.*)")[1]);
        }
        catch (e) {
            index = Math.round(Math.random() * quotes.length) % quotes.length;
        }
        finally {
            if (isNaN(index) || event) {
                index = Math.round(Math.random() * quotes.length) % quotes.length;
            }
        }
    }

    console.log(index);
    quotes[index].hidden = false;
    quotes[index].style.listStyleType= 'none';

    // Change link for copy-paste, etc.
    window.location.hash = "#" + index;

}

var add_buttons = function () {
    var quote_container = document.querySelector('.quotes');
    var quotes = document.querySelectorAll('.quotes .org-ul li');
    var count = quotes.length;

    var nav = document.createElement("div");
    nav.setAttribute('class', 'pagination');
    quote_container.insertBefore(nav, quote_container.firstChild);

    var random = document.createElement("span");
    random.setAttribute('class', 'pagination-item older');
    nav.appendChild(random);

    var random_quote = document.createElement("a");
    random_quote.setAttribute('title', 'Show Random');
    random_quote.setAttribute('href', '#');
    random_quote.setAttribute('onclick', 'show_random_quote(event)');
    random_quote.textContent = "Show Random Quote";
    random.appendChild(random_quote);

    var show = document.createElement("span");
    show.setAttribute('class', 'pagination-item newer');
    nav.appendChild(show);

    var show_quotes = document.createElement("a");
    show_quotes.setAttribute('title', 'Show All Quotes');
    show_quotes.setAttribute('href', '');
    show_quotes.setAttribute('onclick', 'show_all_quotes(event)');
    show_quotes.textContent = "Show All (" + count + ") Quotes";
    show.appendChild(show_quotes);

}

show_random_quote();
add_buttons();
