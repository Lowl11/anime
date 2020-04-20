from django.conf import settings
from django.utils import timezone

# Подключение кастомных классов
from watch.models import Anime
from help.genre import GenreHelper
from utils.dict import Dictionary
from utils.form import FormHelper

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
    
    # возвращает список аниме по жанру
    @staticmethod
    def get_by_genre(genre_name):
        # достаем список привязок аниме-жанр
        genres = GenreHelper.get_genres_by_name(genre_name)

        # TODO возможно есть смысл попытаться избавиться от привязки к типу
        # оставляем из списка только 1 аниме (т.к. аниме много)
        anime_list = Dictionary()
        anime_type = type(Anime)
        anime_list.set_data_type(anime_type)
        for genre in genres:
            anime = genre.anime
            anime_list.add(anime.id, anime)
        
        return AnimeHelper.prepare_anime_list(anime_list.to_list())
    
    # возвращает список аниме по году
    @staticmethod
    def get_by_year(year):
        anime_list = Anime.objects.filter(start_date__year = year)
        return AnimeHelper.prepare_anime_list(anime_list)

    # возвращает определенное аниме по ID
    @staticmethod
    def get_anime_by_id(id):
        anime = Anime.objects.get(pk = id)
        return anime
    
    # заполнение формы значениями существующего аниме
    @staticmethod
    def fill_form(form, anime):
        # TODO понять через какое поле или через какой параметр заполняется textarea
        fields = form.fields
        FormHelper.update_field(fields['title_rus'], anime.title_rus)
        FormHelper.update_field(fields['title_foreign'], anime.title_foreign)
        FormHelper.update_field(fields['season'], anime.season)
        # FormHelper.update_field(fields['description'], anime.description)
        FormHelper.update_field(fields['episodes_quantity'], anime.episodes_quantity)
        FormHelper.update_field(fields['start_date'], anime.start_date)
        return form
    

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # подготовка списка аниме
    @staticmethod
    def prepare_anime_list(anime_list):
        for anime in anime_list:
            anime.genre_links = GenreHelper.anime_genres_links(anime)
        return anime_list
