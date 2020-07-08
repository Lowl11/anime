$(() => {

    let animeManager = new AnimeManager();

});

class AnimeManager {

    AnimeId = 0;
    CommentUrl = "/watch/comment/";
    CommentManager = null;

    constructor() {
        this.AnimeId = $('#anime-id').text();
        this.CommentManager = new CommentManager({'anime_id': this.AnimeId}, "/watch/comment/");
    }

}