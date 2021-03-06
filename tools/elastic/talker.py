import json

# Подключение кастомных классов
from tools import rest
from tools import utils
from tools import logger
from tools import debugger


class ElasticTalker:
    """ ElasticTalker - переговорщик который отправляет запросы в эластик и обрабатывает ответ """

    def __init__(self, url):
        self.url = url
        self.last_request_status = None

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def talk(self, postfix, data, request_type):
        """ запрос в Elastic """

        full_url = self.url + postfix  # site.com:9200/postfix

        # отправляем непосредственно запрос
        response, err = rest.make_request(full_url, json.dumps(data), request_type)

        if err is not None:
            utils.raise_exception(str(err), logger.ELASTIC)
        else:
            if not response.ok:
                err = Exception('Ошибка ElasticSearch. Response: ' + str(response.text))

        return response, err

    def check_status(self):
        """ проверка статуса сервера """

        postfix = '_cat/indices'
        full_url = self.url + postfix
        data = {}

        response, err = rest.make_request(full_url, json.dumps(data), 'GET')

        if err is not None:
            return False

        if response is None:
            return False

        return True
