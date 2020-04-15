from django.conf import settings

# Подключение кастомных классов
from watch.models import Anime
from help.genre import GenreHelper

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    AnimeHelper - управление записями аниме
"""
class AnimeHelper:
    # возвращает все аниме
    @staticmethod
    def get_all():
        anime_list = Anime.objects.all()
        for anime in anime_list:
            anime.genre_links = GenreHelper.anime_genres_links(anime)
        return anime_list
    
    # возвращает определенное аниме по ID
    @staticmethod
    def get_anime_by_id(id):
        anime = Anime.objects.get(pk = id)
        if anime is None:
            return False
        return anime
