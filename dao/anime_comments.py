from watch.models import Anime
from watch.models import AnimeComment


class AnimeCommentsManager:
    @staticmethod
    def get_all(anime):
        comments = AnimeComment.objects.filter(anime = anime)
        return comments

    @staticmethod
    def create(author, anime, text):
        comment = AnimeComment()
        comment.author = author
        comment.anime = anime
        comment.text = text
        comment.save()
