from django.conf import settings
from datetime import date

from tools import utils

class IndexManager:
    def __init__(self, talker):
        self.talker = talker
    
    # возвращает акутальное название индекса
    @staticmethod
    def anime_index_name():
        return 'anime-' + date.today().strftime('%d.%m.%Y')

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################
    
    # возвращает все индексы
    def get_all(self):
        data = {}
        postfix = '_cat/indices'
        response = self.talker.talk(postfix, data, 'GET')

        if response is None:
            utils.raise_exception('Response не вернулся после запроса всех индексов')
        
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

        return indices

    # создание индекса аниме
    def create_anime_index(self):
        data = {
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 2
                },
                "analysis": {
                    "analyzer": {
                        "anime_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "char_filter": [
                                "html_strip"
                            ],
                            "filter": [
                                "lowercase",
                                "asciifolding",
                                "english_stop",
                                "russian_stop"
                            ]
                        }
                    },
                    "filter": {
                        "english_stop": {
                            "type": "stop",
                            "stopwords": "_english_"
                        },
                        "russian_stop": {
                            "type": "stop",
                            "stopwords": "_russian_"
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "title_rus": { "type": "text" },
                    "title_foreign": { "type": "text" },
                    "description": { "type": "text" }
                }
            }
        }
        json_response = self.talker.talk(IndexManager.anime_index_name(), data, 'PUT')
        self.__base_check(json_response)
        return json_response
    
    # удаление индекса
    def delete_anime_index(self):
        data = {}
        json_response = self.talker.talk(IndexManager.anime_index_name(), data, 'DELETE')
        return json_response
    


    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # базовая проверка каждого возвращаемого JSON
    def __base_check(self, response):
        success = utils.try_get_from_array(response, 'acknowledged')
        if success is None:
            utils.raise_exception('Ошибка после запроса на действие с индексом\nResponse: ' + str(response))
        return
    
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
            return self.status + ' | ' + self.name + ' | ' + self.hash_code + ' | ' + self.size
