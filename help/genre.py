from django.conf import settings

# Подключение кастомных классов
from watch.models import Genre, ConstantGenre

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    GenreHelper - вспомогающий класс
"""
class GenreHelper:
    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################
    # Возвращает все жанры аниме
    @staticmethod
    def get_genres():
        genre_list = ConstantGenre.objects.all()
        return genre_list
    
    @staticmethod
    def anime_genres_links(anime):
        anime_genres = GenreHelper.anime_genres(anime)
        length = len(anime_genres)
        html = ''
        for i in range(0, length):
            genre = anime_genres[i]
            html += '<a href="/watch/genre/' + genre.constant_genre.name + '">' + genre.constant_genre.name + '</a>'
            if i != length - 1:
                html += ', '
        return html

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################
    @staticmethod
    def anime_genres(anime):
        genre_list = Genre.objects.filter(anime = anime)
        return genre_list
    
