var httpGetAsync = function (theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

var insertPosts = function (data) {
    var div = document.querySelector('#recent-posts');

    var heading = document.createElement('h3');
    heading.textContent = 'Recent Posts';
    div.appendChild(heading);

    var ul = document.createElement('ul');
    ul.style.paddingLeft = '0px';
    ul.style.listStyleType = 'none';
    div.appendChild(ul);

    JSON.parse(data).forEach(function(elem){
        var li = document.createElement('li');

        var a = document.createElement('a');
        a.textContent = elem.title;
        a.setAttribute('href', elem.loc);
        li.appendChild(a);
        ul.appendChild(li);

        var date = document.createElement('span');
        date.setAttribute('class', 'post-date');
        var d = new Date(elem.date);
        date.textContent = d.toLocaleString(undefined, {day: "numeric", month: "short", year: "numeric"});
        li.appendChild(date);


    });
}

httpGetAsync("/index.json", insertPosts)
