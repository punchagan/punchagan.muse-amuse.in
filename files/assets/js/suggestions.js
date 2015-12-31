function search(){

    var get_search_string = function(){
        var url = document.location.href;
        var search_string = url.replace(/.*\/(.*)/g, "$1");

        if (search_string.length < 32) {
            return search_string;
        } else {

            if (tipuesearch_stop_words.indexOf('html') == -1) {
                tipuesearch_stop_words.push("html");
            }
            var search_terms = search_string.split('-');
            search_terms.forEach(function(term, idx){
                if (tipuesearch_stop_words.indexOf(term)) {
                    search_terms.splice(idx, 1);
                }
            });
            return search_terms.join('-').substring(0, 31);
        }
    };

    var show_results = function(entries) {
        var entries_ul = $('<ul class="entries">');
        if (entries.length == 0) {
            $('#suggestions-loading').text('Sorry no matching posts could be found!');
        } else {
            $('#suggestions-loading').text('Are you looking for any of the following posts?');
            $('#suggestions').append(entries_ul);
            entries.forEach(function(entry){
                var entry_li = $('<a>').attr('href', entry.loc).text(entry.title)
                    .appendTo($('<li>').appendTo(entries_ul));
            });
        };
    };

    $.getJSON('/assets/js/tipuesearch_content.json').done(
        function(data){
            var options = {
                keys: ['text', 'title', 'loc']
            };
            var fuse = new Fuse(data.pages, options);
            var results = fuse.search(get_search_string());
            results.splice(5);
            show_results(results);
        });

};
window.onload = search;
