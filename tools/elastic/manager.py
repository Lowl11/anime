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


class ElasticSearchManager:
    """ ElasticSearchManager - класс помогающий делать всякое с эластиком поверхностно """

    def __init__(self):
        self.url = 'http://127.0.0.1:9200/'
        self.talker = talker(self.url)
        self.index_manager = IndexManager(self.talker)
        self.data_manager = DataManager(self.talker)
        self.searcher = Searcher(self.talker)


    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def check_status(self):
        """ проверка статуса сервера эластика """
        return self.talker.check_status()

    def get_all_indices(self):
        """ возвращает все индексы в эластике """
        return self.index_manager.get_all()

    def delete_index(self, index_name):
        """ удаление индекса """
        self.index_manager.delete_index_by_name(index_name)

    def create_index(self, data_type):
        """ создание индекса """

        if data_type == 'anime':
            self.index_manager.delete_index_by_type(data_type)
            self.index_manager.create_anime_index()
        else:
            Utils.raise_exception('Не поддерживаемый тип данных')

    def fill_index(self, data_type):
        """ заполнение данными """

        if data_type == 'anime':
            self.data_manager.fill_anime_index()
        else:
            Utils.raise_exception('Не поддерживаемый тип данных')

    def search_anime(self, query):
        """ поиск аниме """
        return self.searcher.search_anime(query)

    def define_index_type(self, index_name):
        """ возвращает тип удаляемых данных """

        before_minus = index_name.split('-')
        return before_minus[0]
