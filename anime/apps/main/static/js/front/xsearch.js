class XSearch {

    XSearchObject = null;
    XSearchHiddenObject = null;

    constructor() {
        this.XSearchObject = $('.xsearch input:text');
        this.XSearchHiddenObject = $('.xsearch input:hidden');
        this.BindSearchEvent();
        this.CheckAndPasteQuery();
    }

    BindSearchEvent() {
        this.XSearchObject.off('keyup.XSearchKeyUp');
        this.XSearchObject.on('keyup.XSearchKeyUp', (e) => {
            if (e.which == 13) {
                let query = this.XSearchObject.val();
                console.log(query);
                if (query.length >= 4) {
                    window.location = "/watch/xsearch/?query=" + query;
                }
            }
        });
    }

    CheckAndPasteQuery() {
        let queryPlaceholder = this.XSearchHiddenObject.val();
        if (queryPlaceholder != null || queryPlaceholder != undefined) {
            if (queryPlaceholder.length > 0) {
                this.XSearchObject.val(queryPlaceholder);
            }
        }
    }

}

$(function() {

    var xsearch = new XSearch();

});
