from django.conf import settings

# Подключение кастомных классов
from watch.models import Anime
from help.genre import GenreHelper
from utils.dict import Dictionary

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    AnimeHelper - управление записями аниме
"""
class AnimeHelper:
    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает все аниме
    @staticmethod
    def get_all():
        anime_list = Anime.objects.all()
        return AnimeHelper.prepare_anime_list(anime_list)
    
    @staticmethod
    def get_by_genre(genre_name):
        genres = GenreHelper.get_genres_by_name(genre_name)

        # оставляем из списка только 1 аниме
        anime_list = Dictionary()
        anime_type = type(Anime)
        anime_list.set_data_type(anime_type)
        for genre in genres:
            anime = genre.anime
            anime_list.add(anime.id, anime)
        
        return AnimeHelper.prepare_anime_list(anime_list.to_list())
    
    # возвращает определенное аниме по ID
    @staticmethod
    def get_anime_by_id(id):
        anime = Anime.objects.get(pk = id)
        if anime is None:
            return False
        return anime
    

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # подготовка списка аниме
    @staticmethod
    def prepare_anime_list(anime_list):
        for anime in anime_list:
            anime.genre_links = GenreHelper.anime_genres_links(anime)
        return anime_list
