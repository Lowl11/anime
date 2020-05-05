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

class ElasticSearchManager:
    def __init__(self):
        self.url = 'http://127.0.0.1:9200/'
        self.talker = talker(self.url)
        self.index_manager = IndexManager(self.talker)
        self.data_manager = DataManager(self.talker)


    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

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
        postfix = self.anime_index_name() + '/_search'
        request_type = 'POST'
        data = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title_rus", "title_foreign", "description"],
                    "prefix_length": 2,
                    "max_expansions": 1
                }
            },
            "suggest": {
                "title_rus_suggestion": {
                    "text": query,
                    "term": {
                        "field": "title_rus"
                    }
                },
                "title_foreign_suggestion": {
                    "text": query,
                    "term": {
                        "field": "title_foreign"
                    }
                },
                "description_suggestion": {
                    "text": query,
                    "term": {
                        "field": "description"
                    }
                }
            }
        }

        response = self.make_request(postfix, json.dumps(data), request_type)

        if response is None:
            return response

        json_response = response.json()
        if Utils.try_get_from_array(json_response, 'status') == '400':
            return None
        
        out_hits = json_response['hits']
        inside_hits = out_hits['hits']

        anime_list = []
        for hit in inside_hits:
            anime = hit['_source']
            anime_list.append(AnimeManager.parse(anime))
        
        if len(inside_hits) == 0:
            suggest = json_response['suggest']

            description_suggestions = suggest['description_suggestion']
            title_rus_suggestions = suggest['title_rus_suggestion']
            title_foreign_suggestions = suggest['title_foreign_suggestion']

            description_options = description_suggestions[0]['options']
            title_rus_options = title_rus_suggestions[0]['options']
            title_foreign_options = title_foreign_suggestions[0]['options']

            description_query = { 'score': 0 }
            title_rus_query = { 'score': 0 }
            title_foreign_query = { 'score': 0 }

            if len(description_options) > 0:
                description_query = description_options[0]
            
            if len(title_rus_options) > 0:
                title_rus_query = title_rus_options[0]
            
            if len(title_foreign_options) > 0:
                title_foreign_query = title_foreign_options[0]
            
            biggest = title_rus_query
            if biggest['score'] < title_foreign_query['score']:
                biggest = title_foreign_query
            
            if biggest['score'] < description_query['score']:
                biggest = description_query
            
            if biggest['score'] > 0:
                return self.search_anime(biggest['text'])

        return anime_list


    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def make_request(self, postfix, data, request_type):
        response = None
        full_url = self.url + postfix
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        try:
            if request_type == 'POST':
                response = requests.post(full_url, data = data, headers = headers)
            elif request_type == 'GET':
                response = requests.get(full_url, data = data, headers = headers)
            elif request_type == 'PUT':
                response = requests.put(full_url, data = data, headers = headers)
            elif request_type == 'DELETE':
                response = requests.delete(full_url, data = data, headers = headers)

            if response.status_code != 200 or response.status_code == 201:
                return None
        except:
            pass
        
        return response
    
    def anime_index_name(self):
        return 'anime-' + date.today().strftime('%d.%m.%Y')
