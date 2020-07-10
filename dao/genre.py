from django.conf import settings

# Подключение кастомных классов
from watch.models import Genre, ConstantGenre
from .base import BaseDaoManager

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


class GenreManager(BaseDaoManager):
    """ GenreManager - вспомогающий класс """

    def __init__(self):
        super(GenreManager, self).__init__(ConstantGenre)

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################
    
    # возвращает список жанров одного аниме как список ссылок HTML
    @staticmethod
    def anime_genres_links(anime):
        anime_genres = GenreManager.anime_genres(anime)
        length = len(anime_genres)
        html = ''
        for i in range(0, length):
            genre = anime_genres[i]
            html += '<a href="/watch/genre/' + genre.constant_genre.name + '">' + genre.constant_genre.name + '</a>'
            if i != length - 1:
                html += ', '
        return html
    
    # возвращает список привязок аниме-жанр по названию жанра
    @staticmethod
    def get_genres_by_name(genre_name):
        genres = Genre.objects.filter(constant_genre__name = genre_name)
        return genres


    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает список жанров по аниме
    @staticmethod
    def anime_genres(anime):
        genre_list = Genre.objects.filter(anime = anime)
        return genre_list
    
