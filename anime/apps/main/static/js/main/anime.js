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

                $.ajaxSetup({
                    beforeSend: (xhr, settings) => {
                        xhr.setRequestHeader("X-CSRFToken", this.GetCSRFToken());
                    }
                });
                $.ajax({
                    type: "POST",
                    url: "/watch/comment/",
                    data: data,
                    cache: false,
                    success: (data) => {
                        if (data == "1") {
                            window.location.reload();
                        }
                    },
                    error: (jqXHR, exception) => {
                        logger.HandleException(jqXHR, exception, this.URL, data);
                    }
                });
            }
        });
    }

    GetCSRFToken() {
        let name = 'csrftoken';
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

}