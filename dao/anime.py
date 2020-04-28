from django.conf import settings
from django.utils import timezone
from datetime import datetime

# Подключение кастомных классов
from watch.models import Anime
from .genre import GenreManager
from tools.dict import Dictionary
from tools import forms as FormManager
from tools import debugger

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
    
    # обновление данных аниме по id
    @staticmethod
    def update_anime_by_id(id, updated):
        try:
            anime = AnimeManager.get_anime_by_id(id)
            anime.title_rus = updated['title_rus']
            anime.title_foreign = updated['title_foreign']
            anime.description = updated['description']
            anime.season = updated['season']
            anime.episodes_quantity = updated['episodes_quantity']
            anime.start_date = updated['start_date']
            # TODO сделать upload обложки (и вообще файлов)
            anime.save()
        except:
            return False
        return True
    
    # заполнение формы значениями существующего аниме
    @staticmethod
    def fill_form(form, anime):
        # TODO понять через какое поле или через какой параметр заполняется textarea
        fields = form.fields
        FormManager.update_field(fields['title_rus'], anime.title_rus)
        FormManager.update_field(fields['title_foreign'], anime.title_foreign)
        FormManager.update_field(fields['season'], anime.season)
        FormManager.update_field(fields['description'], anime.description)
        FormManager.update_field(fields['episodes_quantity'], anime.episodes_quantity)
        FormManager.update_field(fields['start_date'], anime.start_date)
        FormManager.update_field(fields['image'], anime.image.url)
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
    
    # превратить массив в объект
    @staticmethod
    def parse(array):
        anime = Anime()
        anime.id = array['id']
        anime.title_rus = array['title_rus']
        anime.title_foreign = array['title_foreign']
        anime.description = array['description']
        anime.start_date = datetime.strptime(array['start_date'], '%Y-%m-%d')
        anime.season = int(array['season'])
        anime.episodes_quantity = int(array['episodes_quantity'])
        anime.image = open('media/anime/one_piece.png')
        return anime

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # подготовка списка аниме
    @staticmethod
    def prepare_anime_list(anime_list):
        # обязательно сортировка первая
        anime_list = AnimeManager.sort(anime_list)
        for anime in anime_list:
            anime.genre_links = GenreManager.anime_genres_links(anime)
        return anime_list
    
    # сортировка аниме листа
    @staticmethod
    def sort(anime_list):
        # пока что так, сортировка по дате (DESC)
        if type(anime_list) == type([]):
            return AnimeManager.sort_list(anime_list)
        return anime_list.order_by('-start_date')
    
    # сортировка аниме листа list
    @staticmethod
    def sort_list(anime_list):
        for i in range(0, len(anime_list)):
            for j in range(i+1, len(anime_list)):
                # < desc
                # > asc
                if anime_list[i].start_date < anime_list[j].start_date:
                    anime_list[i], anime_list[j] = anime_list[j], anime_list[i]
        return anime_list
