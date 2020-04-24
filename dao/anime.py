from django.conf import settings
from django.utils import timezone

# Подключение кастомных классов
from watch.models import Anime
from .genre import GenreManager
from tools.dict import Dictionary
from tools import forms as FormManager

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    AnimeManager - управление записями аниме
"""
class AnimeManager:
    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает все аниме
    @staticmethod
    def get_all():
        anime_list = Anime.objects.all()
        return AnimeManager.prepare_anime_list(anime_list)
    
    # возвращает список аниме по жанру
    @staticmethod
    def get_by_genre(genre_name):
        # достаем список привязок аниме-жанр
        genres = GenreManager.get_genres_by_name(genre_name)

        # TODO возможно есть смысл попытаться избавиться от привязки к типу
        # оставляем из списка только 1 аниме (т.к. аниме много)
        anime_list = Dictionary()
        anime_type = type(Anime)
        anime_list.set_data_type(anime_type)
        for genre in genres:
            anime = genre.anime
            anime_list.add(anime.id, anime)
        
        return AnimeManager.prepare_anime_list(anime_list.to_list())
    
    # возвращает список аниме по году
    @staticmethod
    def get_by_year(year):
        anime_list = Anime.objects.filter(start_date__year = year)
        return AnimeManager.prepare_anime_list(anime_list)

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
        FormManager.update_field(fields['title_rus'], anime.title_rus)
        FormManager.update_field(fields['title_foreign'], anime.title_foreign)
        FormManager.update_field(fields['season'], anime.season)
        # FormManager.update_field(fields['description'], anime.description)
        FormManager.update_field(fields['episodes_quantity'], anime.episodes_quantity)
        FormManager.update_field(fields['start_date'], anime.start_date)
        return form
    
    # поиск аниме
    @staticmethod
    def search(query):
        anime_list = []
        anime_list.extend(Anime.objects.filter(title_rus__icontains = query))
        anime_list.extend(Anime.objects.filter(title_foreign__icontains = query))
        anime_list.extend(Anime.objects.filter(description__icontains = query))

        result_list = Dictionary()
        for anime in anime_list:
            result_list.add(anime.id, anime)

        return result_list.to_list()

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # подготовка списка аниме
    @staticmethod
    def prepare_anime_list(anime_list):
        for anime in anime_list:
            anime.genre_links = GenreManager.anime_genres_links(anime)
        return anime_list
