import requests
import json
import os

from django.conf import settings
from datetime import date

# Подключение кастомных классов
from tools import rest
from tools import utils

'''
    ElasticTalker - переговорщик который отправляет запросы в эластик и обрабатывает ответ
'''
class ElasticTalker:
    def __init__(self, url):
        self.url = url
        self.last_request_status = None
    

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################
    
    # запрос в Elastic
    def talk(self, postfix, data, request_type):
        full_url = self.url + postfix # site.com:9200/postfix

        # отправляем непосредственно запрос
        response = rest.make_request(full_url, json.dumps(data), request_type)

        self.last_request_status = 1 # последний запрос был успешным
        if response is None:
            utils.raise_exception('Ошибка соеденения сервера с ElasticSearch')
            self.last_request_status = 2 # последний запрос был с ошибкой
        
        try:
            # бывает такое что ответ не в виде json а просто в виде текста (читать следующий коммент)
            json_response = response.json()
        except:
            # по этому возвращаем сам респонс как текст
            return response

        return json_response
