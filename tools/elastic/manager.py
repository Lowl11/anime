# Подключение кастомных классов
from tools.elastic.data import DataManager
from tools.elastic.index import IndexManager
from tools.elastic.searcher import Searcher
from tools.elastic.talker import ElasticTalker as talker
from tools import utils as Utils
from tools import logger
from dao.anime import AnimeManager


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
        logger.write('Пользователь запросил Список всех индексов', logger.ELASTIC)
        return self.index_manager.get_all()

    def delete_index(self, index_name):
        """ удаление индекса """
        logger.write('Пользователь запросил удаление индекса "' + str(index_name) + '"', logger.ELASTIC)
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
            Utils.raise_exception('Не поддерживаемый тип данных', logger.ELASTIC)

    def search_anime(self, query):
        """ поиск аниме """
        anime_list = self.searcher.search_anime(query)
        if anime_list is not None:
            anime_list = AnimeManager.prepare_anime_list(anime_list)
            result_quantity = str(len(anime_list))
            logger.write(
                'Пользователь запросил поиск по запросу "' + query + '"\nКол-во результатов: ' + result_quantity,
                logger.ELASTIC)
        return anime_list

    def define_index_type(self, index_name):
        """ возвращает тип удаляемых данных """

        before_minus = index_name.split('-')
        return before_minus[0]
