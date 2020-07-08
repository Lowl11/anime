$(() => {

    let animeManager = new AnimeManager();

});

class AnimeManager {

    AnimeId = 0;
    CreateCommentUrl = "/watch/comment/";
    DeleteCommentUrl = "/watch/delete-comment/";
    CommentManager = null;

    constructor() {
        this.AnimeId = $('#anime-id').text();
        this.InitializeCommentManager();
    }

    InitializeCommentManager() {
        let data = {
            'anime_id': this.AnimeId
        };
        this.CommentManager = new CommentManager(
            data,
            this.CreateCommentUrl,
            this.DeleteCommentUrl
        );
    }

}