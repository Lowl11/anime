import requests
import json
import os

# Подключение кастомных классов
from utils.debugger import Debugger
from utils.utils import Utils

class ElasticSearchHelper:
    def __init__(self):
        self.url = ''

    def get_all_indices(self):
        data = ''
        request_type = 'GET'
        updated_url = self.url + '/_cat/indices'
        response = self.make_request(updated_url, data, request_type)

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
            index.size = words[8]
            indices.append(index)
        
        return indices
    
    def make_request(self, url, data, request_type):
        response = None
        if request_type == 'POST':
            response = requests.post(url, data = data)
        elif request_type == 'GET':
            response = requests.get(url, data = data)
        elif request_type == 'PUT':
            response = requests.get(url, data = data)
        
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
        
        def __str__(self):
            return self.status + ' | ' + self.name + ' | ' + self.hash_code + ' | ' + self.size
