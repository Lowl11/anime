import json

# Подключение кастомных классов
from tools.elastic.index import IndexManager
from dao.anime import AnimeManager


'''
    DataManager - CRUD для данных заполняемых в индексы
'''
class DataManager:
    def __init__(self, talker):
        self.talker = talker
    

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################
    
    # заполняет индекс аниме анимешками
    def fill_anime_index(self):
        postfix = self.__anime_index_name() + '/_doc'
        anime_list = AnimeManager.get_all() # берем все анимешки
        objects_list = AnimeManager.parse_to_objects(anime_list) # превращаем их в объекты (для JSON)
        for anime in objects_list: # по очереди заполянем индекс анимешками
            self.__create_doc(postfix, anime)


    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # создает запись в индексе
    def __create_doc(self, postfix, data):
        response = self.talker.talk(postfix, data, 'POST')

    # возвращает актуальное название индекса аниме
    def __anime_index_name(self):
        return IndexManager.anime_index_name()
