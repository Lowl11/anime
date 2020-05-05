import json

from tools.elastic.index import IndexManager
from dao.anime import AnimeManager

class DataManager:
    def __init__(self, talker):
        self.talker = talker
    
    def fill_anime_index(self):
        postfix = self.__anime_index_name() + '/_doc'
        anime_list = AnimeManager.get_all() # берем все анимешки
        objects_list = AnimeManager.parse_to_objects(anime_list) # превращаем их в объекты (для JSON)
        for anime in objects_list:
            self.create_doc(postfix, anime)
    
    def create_doc(self, postfix, data):
        response = self.talker.talk(postfix, data, 'POST')

    def __anime_index_name(self):
        return IndexManager.anime_index_name()
