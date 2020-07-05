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


class AnimeManager:
    """ AnimeManager - управление записями аниме """

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    @staticmethod
    def get_all():
        """ возвращает все аниме """
        anime_list = Anime.objects.all()
        return AnimeManager.prepare_anime_list(anime_list)

    @staticmethod
    def get_by_genre(genre_name):
        """ возвращает список аниме по жанру """

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

    @staticmethod
    def get_by_year(year):
        """ возвращает список аниме по году """
        anime_list = Anime.objects.filter(start_date__year = year)
        return AnimeManager.prepare_anime_list(anime_list)

    @staticmethod
    def get_anime_by_id(id):
        """ возвращает определенное аниме по ID """
        anime = Anime.objects.get(pk = id)
        return anime

    @staticmethod
    def update_anime_by_id(id, updated):
        """ обновление данных аниме по id """

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

    @staticmethod
    def fill_form(form, anime):
        """ заполнение формы значениями существующего аниме """

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

    @staticmethod
    def search(query):
        """ поиск аниме """

        anime_list = []
        anime_list.extend(Anime.objects.filter(title_rus__icontains = query))
        anime_list.extend(Anime.objects.filter(title_foreign__icontains = query))
        anime_list.extend(Anime.objects.filter(description__icontains = query))

        result_list = Dictionary()
        for anime in anime_list:
            result_list.add(anime.id, anime)

        return result_list.to_list()

    @staticmethod
    def parse(array):
        """ превращение объекта в аниме """

        anime = Anime()
        anime.id = array['id']
        anime.title_rus = array['title_rus']
        anime.title_foreign = array['title_foreign']
        anime.description = array['description']
        anime.start_date = datetime.strptime(array['start_date'], '%Y-%m-%d')
        anime.season = int(array['season'])
        anime.episodes_quantity = int(array['episodes_quantity'])
        anime.image = array['image']
        return anime

    @staticmethod
    def parse_to_objects(anime_list):
        """ проверащение аниме списка в список объектов """

        objects_list = []
        for anime in anime_list:
            data = {
                'id': str(anime.id),
                'title_rus': anime.title_rus,
                'title_foreign': anime.title_foreign,
                'description': anime.description,
                'season': str(anime.season),
                'episodes_quantity': str(anime.episodes_quantity),
                'start_date': str(anime.start_date),
                'image': str(anime.image),
                'tags': anime.tags
            }
            objects_list.append(data)
        return objects_list


    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    @staticmethod
    def prepare_anime_list(anime_list):
        """ подготовка списка аниме """

        # обязательно сортировка первая
        anime_list = AnimeManager.sort(anime_list)
        for anime in anime_list:
            anime.genre_links = GenreManager.anime_genres_links(anime)
        return anime_list

    @staticmethod
    def sort(anime_list):
        """ сортировка аниме листа """

        # пока что так, сортировка по дате (DESC)
        if type(anime_list) == type([]):
            return AnimeManager.sort_list(anime_list)
        return anime_list.order_by('-start_date')

    @staticmethod
    def sort_list(anime_list):
        """ сортировка аниме листа list """

        for i in range(0, len(anime_list)):
            for j in range(i+1, len(anime_list)):
                # < desc
                # > asc
                if anime_list[i].start_date < anime_list[j].start_date:
                    anime_list[i], anime_list[j] = anime_list[j], anime_list[i]
        return anime_list
