$(() => {

    let xsearch = $('.xsearch input');
    xsearch.off('keyup.XSearch');
    xsearch.on('keyup.XSearch', (e) => {
        if (e.which == 13) {
            let query = xsearch.val();
            if (query.length >= 4) {
                window.location = "/watch/xsearch/?query=" + query;
            }
        }
    });

    let queryPlaceholder = $('.xsearch input:hidden').val();
    if (queryPlaceholder.length > 0) {
        xsearch.val(queryPlaceholder);
    }

});