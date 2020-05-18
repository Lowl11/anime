import requests
import json
import os

from django.conf import settings
from datetime import date

# Подключение кастомных классов
from tools import debugger
from tools import utils as Utils
from dao.anime import AnimeManager
from tools.elastic.talker import ElasticTalker as talker
from tools.elastic.index import IndexManager
from tools.elastic.data import DataManager
from tools.elastic.searcher import Searcher

'''
    ElasticSearchManager - класс помогающий делать всякое с эластиком поверхностно
'''
class ElasticSearchManager:
    def __init__(self):
        self.url = 'http://127.0.0.1:9200/'
        self.talker = talker(self.url)
        self.index_manager = IndexManager(self.talker)
        self.data_manager = DataManager(self.talker)
        self.searcher = Searcher(self.talker)


    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # проверка статуса сервера эластика
    def check_status(self):
        return self.talker.check_status()

    # возвращает все индексы в эластике
    def get_all_indices(self):
        return self.index_manager.get_all()
    
    # удаление индекса
    def delete_index(self, data_type):
        if data_type == 'anime':
            self.index_manager.delete_anime_index()
        else:
            Utils.raise_exception('Не поддерживаемый тип данных')
    
    # создание индекса
    def create_index(self, data_type):
        if data_type == 'anime':
            self.index_manager.delete_anime_index()
            self.index_manager.create_anime_index()
        else:
            Utils.raise_exception('Не поддерживаемый тип данных')
        
    # заполнение данными
    def fill_index(self, data_type):
        if data_type == 'anime':
            self.data_manager.fill_anime_index()
        else:
            Utils.raise_exception('Не поддерживаемый тип данных')
    
    # поиск аниме
    def search_anime(self, query):
        return self.searcher.search_anime(query)
