import requests
import json
import os

# Подключение кастомных классов
from utils import debugger
from utils import utils as Utils

class ElasticSearchHelper:
    def __init__(self):
        self.url = ''


    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает все индексы в эластике
    def get_all_indices(self):
        data = ''
        request_type = 'GET'
        postfix = '/_cat/indices'
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
        postfix = '/' + index_name
        response = self.make_request(postfix, {}, 'DELETE')

        if response is None:
            return response
        
        json_response = response.json()

        if json_response['acknowledged'] == True:
            return True
        
        return False
    
    # создание индекса
    def create_index(self, index_name):
        postfix = '/' + index_name
        response = self.make_request(postfix, {}, 'PUT')

        if response is None:
            return response

        json_response = response.json()

        if json_response['acknowledged'] == True:
            return True
        
        return False
    

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def make_request(self, postfix, data, request_type):
        response = None
        full_url = self.url + postfix
        if request_type == 'POST':
            response = requests.post(full_url, data = data)
        elif request_type == 'GET':
            response = requests.get(full_url, data = data)
        elif request_type == 'PUT':
            response = requests.put(full_url, data = data)
        elif request_type == 'DELETE':
            response = requests.delete(full_url, data = data)
        
        if response.status_code != 200:
            return None
        return response
    
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
