from datetime import date

# Подключение кастомных классов
from tools import utils
from tools import logger


class IndexManager:
    """ IndexManager - CRUD для индексов эластика """

    def __init__(self, talker):
        self.talker = talker

    @staticmethod
    def anime_index_name():
        """ возвращает акутальное название индекса """
        return 'anime-' + date.today().strftime('%d.%m.%Y')

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def get_all(self):
        """ возвращает все индексы """

        data = {}
        postfix = '_cat/indices'
        response = self.talker.talk(postfix, data, 'GET')

        if response is None:
            return

        text = response.text
        lines = text.splitlines()

        indices = []
        for line in lines:
            words = utils.erase_empty_strings(line.split(' '))
            index = self.Index()
            index.status = words[0]
            index.name = words[2]
            index.hash_code = words[3]
            index.docs_count = words[6]
            index.delete_count = words[7]
            index.size = words[8]
            indices.append(index)

        return self.__sort_indices(indices)

    def create_anime_index(self):
        """ создание индекса аниме """

        fields = ['title_rus', 'title_foreign', 'description']
        data = {
            "settings": {
                "index": self.__build_index_settings(),
                "analysis": {
                    "analyzer": self.__build_anime_analyzer(),
                    "filter": self.__default_lang_filters()
                }
            }
        }
        data['mappings'] = self.__build_mappings(fields)
        json_response = self.talker.talk(IndexManager.anime_index_name(), data, 'PUT')
        self.__base_check(json_response)
        return json_response

    def delete_index_by_type(self, index_data_type):
        """ удаление индекса по типу индекса """

        index_name = None
        if index_data_type == 'anime':
            index_name = IndexManager.anime_index_name()

        return self.delete_index_by_name(index_name)

    def delete_index_by_name(self, index_name):
        """ удаление индекса по названию индекса """

        data = {}
        json_response = None
        if index_name is not None:
            json_response = self.talker.talk(index_name, data, 'DELETE')
        return json_response

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def __base_check(self, response):
        """ базовая проверка каждого возвращаемого JSON """

        # после взаимодействия с индексами эластик возвращает acknowledged
        success = utils.try_get_from_array(response, 'acknowledged')
        if success is None:
            utils.raise_exception('Ошибка возвращаемого json.\nResponse: ' + str(response), logger.ELASTIC)
        return

    def __build_anime_analyzer(self):
        """ анализатор аниме индекса (конкретно под данные аниме) """

        anime_analyzer = {
            'anime_analyzer': {
                'type': 'custom',
                "tokenizer": "standard",
                "char_filter": [
                    "html_strip"
                ],
                'filter': self.__default_text_filters()
            }
        }

        return anime_analyzer

    def __build_index_settings(self):
        """ настройки индекса типа кол-ва шардов """

        index_settings = {
            "number_of_shards": 3,
            "number_of_replicas": 2
        }
        return index_settings

    def __build_mappings(self, fields):
        """ строит маппинг (структуру) данных судя по заданным полям """

        properties = {}
        for field in fields:
            properties[field] = {'type': 'text', 'analyzer': 'anime_analyzer'}
        mappings = {
            'properties': properties
        }
        return mappings

    def __default_text_filters(self):
        """ дефолтные текстовые фильтры """

        return ["lowercase",
                "asciifolding",
                "english_stop",
                "russian_stop",
                "anime_synonyms"]

    def __default_lang_filters(self):
        """ дефолтные языковые фильтры """
        # TODO нужно добавить каждой записи теги по которым будет поиск
        synonyms = ["дъявол, демон", "сёнен, наруто, хвост феи, ван пис"]

        return {
            "english_stop": {
                "type": "stop",
                "stopwords": "_english_"
            },
            "russian_stop": {
                "type": "stop",
                "stopwords": "_russian_"
            },
            "anime_synonyms": {
                "type": "synonym",
                "synonyms": synonyms,
                "tokenizer": "standard"
            }
        }

    def __sort_indices(self, indices):
        """ сортировка индексов """

        # TODO нужно добавить сортировку по месяцам
        length = len(indices)
        for i in range(length):
            for j in range(i + 1, length):
                if indices[i].name > indices[j].name:
                    indices[i], indices[j] = indices[j], indices[i]
        return indices

    class Index:
        def __init__(self):
            # yellow open test HNYXPGoRSjKBIJTot-e9oA 1 1 0 0 283b 283b
            self.status = ''
            self.name = ''
            self.hash_code = ''
            self.size = ''
            self.docs_count = 0
            self.delete_count = 0

        def __str__(self):
            return self.status + ' | ' + self.name + ' | ' + self.hash_code + ' | ' + self.size + ' | ' + self.size
