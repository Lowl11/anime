from django.conf import settings
from datetime import date

from tools import utils

class IndexManager:
    def __init__(self, talker):
        self.talker = talker

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
        json_response = self.talker.talk(self.__anime_index_name(), data, 'PUT')
        self.__base_check(json_response)
        return json_response
    
    # удаление индекса
    def delete_anime_index(self):
        data = {}
        json_response = self.talker.talk(self.__anime_index_name(), data, 'DELETE')
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

    # возвращает акутальное название индекса
    def __anime_index_name(self):
        return 'anime-' + date.today().strftime('%d.%m.%Y')
