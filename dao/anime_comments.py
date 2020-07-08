from datetime import datetime

from watch.models import Anime
from watch.models import AnimeComment
from tools import logger


class AnimeCommentsManager:
    @staticmethod
    def get_all(anime):
        comments = AnimeComment.objects.filter(anime = anime)
        return reversed(comments)

    @staticmethod
    def delete(pk):
        try:
            comment = AnimeComment.objects.get(pk=pk)
            comment.delete()
        except Exception as error:
            logger.write('Не получилось удалить комментарий с ID: ' + str(pk) + '. Message: ' + str(error), logger.HTTP)
            return False
        return True

    @staticmethod
    def create(author, anime, text):
        comment = AnimeComment()
        comment.author = author
        comment.anime = anime
        comment.text = text
        comment.publish_date = datetime.now()
        comment.save()
        return comment
