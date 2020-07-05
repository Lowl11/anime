$(() => {

    let animeManager = new AnimeManager();

});

class AnimeManager {

    CommentTextArea = $('.send-comment-textarea');
    CommentSend = $('.send-comment-button');
    AnimeId = 0;
    URL = window.location.href;

    constructor() {
        this.AnimeId = $('#anime-id').text();
        this.BindActions();
    }

    BindActions() {
        this.CommentSend.off('click.SendComment');
        this.CommentSend.on('click.SendComment', () => {
            let text = this.CommentTextArea.val();
            if (text.length > 5) {
                let data = {
                    'text': text,
                    'anime_id': this.AnimeId
                };

                let url = "/watch/comment/";
                let onSuccess = (successData) => {
                    if (successData == "1")
                        window.location.reload();
                };

                Utils.AjaxRequest(url, data, onSuccess);
            }
        });
    }

}