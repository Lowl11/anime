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

});