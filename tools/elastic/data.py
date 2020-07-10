import json

# Подключение кастомных классов
from tools.elastic.index import IndexManager
from dao.anime import AnimeManager

anime_manager = AnimeManager()


class DataManager:
    """ DataManager - CRUD для данных заполняемых в индексы """

    def __init__(self, talker):
        self.talker = talker

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def fill_anime_index(self):
        """ заполняет индекс аниме анимешками """

        postfix = self.__anime_index_name() + '/_doc'
        anime_list = anime_manager.get_all()  # берем все анимешки
        objects_list = AnimeManager.parse_to_objects(anime_list)  # превращаем их в объекты (для JSON)
        for anime in objects_list:  # по очереди заполянем индекс анимешками
            self.__create_doc(postfix, anime)

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def __create_doc(self, postfix, data):
        """ создает запись в индексе """
        response = self.talker.talk(postfix, data, 'POST')

    def __anime_index_name(self):
        """ возвращает актуальное название индекса аниме """
        return IndexManager.anime_index_name()
