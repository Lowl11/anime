import requests
import json
import os

from django.conf import settings
from datetime import date

# Подключение кастомных классов
from . import debugger
from . import utils as Utils
from dao.anime import AnimeManager

class ElasticSearchManager:
    def __init__(self):
        self.url = 'http://127.0.0.1:9200/'


    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает все индексы в эластике
    def get_all_indices(self):
        data = {}
        request_type = 'GET'
        postfix = '_cat/indices'
        response = self.make_request(postfix, data, request_type)

        if response is None:
            return response

        text = response.text
        lines = text.splitlines()

        indices = []
        for line in lines:
            words = Utils.erase_empty_strings(line.split(' '))
            index = self.Index()
            index.status = words[0]
            index.name = words[2]
            index.hash_code = words[3]
            index.docs_count = words[6]
            index.delete_count = words[7]
            index.size = words[8]
            indices.append(index)
        
        return indices
    
    # удаляет индекс по имени
    def delete_index(self, index_name):
        postfix = index_name
        response = self.make_request(postfix, {}, 'DELETE')

        if response is None:
            return response
        
        json_response = response.json()

        if json_response['acknowledged'] == True:
            return True
        
        return False
    
    # создание индекса
    def create_index(self, index_name):
        postfix = index_name
        response = self.make_request(postfix, {}, 'PUT')

        if response is None:
            return response

        json_response = response.json()

        if json_response['acknowledged'] == True:
            return True
        
        return False
    
    # удаление индекса
    def delete_index(self, index_name):
        postfix = index_name
        response = self.make_request(postfix, {}, 'DELETE')

        if response is None:
            return response

        json_response = response.json()

        if json_response['acknowledged'] == True:
            return True
        
        return False
    
    # заполнение индекса
    def fill_index_by_anime(self):
        postfix = self.anime_index_name() + '/_doc'
        anime_list = AnimeManager.get_all()
        for anime in anime_list:
            data = {
                'id': str(anime.id),
                'title_rus': anime.title_rus,
                'title_foreign': anime.title_foreign,
                'description': anime.description,
                'season': str(anime.season),
                'episodes_quantity': str(anime.episodes_quantity),
                'start_date': str(anime.start_date)
            }
            self.create_doc(postfix, json.dumps(data))
        return
    
    # создание одной записи
    def create_doc(self, postfix, data):
        response = self.make_request(postfix, data, 'POST')

        if response is None:
            return response
        
        json_response = response.json()

        if json_response['result'] == 'created':
            return True

        return False
    
    # поиск аниме
    def search_anime(self, query):
        postfix = self.anime_index_name() + '/_search'
        request_type = 'POST'
        data = {
            'query': {
                'multi_match': {
                    'query': query,
                    'fields': ['title_rus', 'title_foreign', 'description']
                }
            }
        }

        response = self.make_request(postfix, data, request_type)

        if response is None:
            return response

        json_response = response.json()

        debugger.write(json_response, 'Json Response: ')

        return True


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
                debugger.write(response.text, 'Response:')
            elif request_type == 'GET':
                response = requests.get(full_url, data = data, headers = headers)
            elif request_type == 'PUT':
                response = requests.put(full_url, data = data, headers = headers)
            elif request_type == 'DELETE':
                response = requests.delete(full_url, data = data, headers = headers)
            
            if response.status_code != 200:
                return None
        except:
            pass
        
        return response
    
    # возвращает акутальное название индекса
    def anime_index_name(self):
        return 'anime-' + date.today().strftime('%d.%m.%Y')
    
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
