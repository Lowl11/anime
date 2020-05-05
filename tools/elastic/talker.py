import requests
import json
import os

from django.conf import settings
from datetime import date

# Подключение кастомных классов
from tools import rest
from tools import utils

class ElasticTalker:
    def __init__(self, url):
        self.url = url
        self.last_request_status = None
    

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################
    
    # запрос в Elastic
    def talk(self, postfix, data, request_type):
        full_url = self.url + postfix
        response = rest.make_request(full_url, json.dumps(data), request_type)

        self.last_request_status = 1
        if response is None:
            utils.raise_exception('Ошибка соеденения сервера с ElasticSearch')
            self.last_request_status = 2
        
        try:
            json_response = response.json()
        except:
            return response

        return json_response
    

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def __private_method(self):
        return False
