var hide_all_quotes = function(quotes) {
    for (i=0; i<quotes.length; i++) {
        quotes[i].hidden = true;
    }
}

var show_all_quotes = function() {
    var quotes = document.getElementsByClassName('quotes')[0].getElementsByClassName('org-ul')[0].getElementsByTagName('li');
    for (i=0; i<quotes.length; i++) {
        quotes[i].hidden = false;
    }
}

var show_random_quote = function(event) {

    if (event) {
        event.preventDefault();
    }

    var quotes = document.getElementsByClassName('quotes')[0].getElementsByClassName('org-ul')[0].getElementsByTagName('li');
    hide_all_quotes(quotes);

    var index;
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

    console.log(index);
    quotes[index].hidden = false;

    // Change link for copy-paste, etc.
    window.location.hash = "#" + index;


}

var add_buttons = function () {
    var quote_container = document.getElementsByClassName('quotes')[0];
    var quotes = quote_container.getElementsByClassName('org-ul')[0].getElementsByTagName('li');
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
    show_quotes.setAttribute('onclick', 'show_all_quotes()');
    show_quotes.textContent = "Show All (" + count + ") Quotes";
    show.appendChild(show_quotes);

}

show_random_quote();
add_buttons();
