import requests
import json
import os

from tools import utils

# делает запрос по урлу
def make_request(url, data, request_type, headers = None):
    if headers is None: # по дефолту будем отправлять JSON
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # try/except потому что нужно будет отловить ошибку и логировать (или выкинуть)
    try:
        
        if request_type == 'POST':
            response = requests.post(url, data = data, headers = headers)
        elif request_type == 'GET':
            response = requests.get(url, data = data, headers = headers)
        elif request_type == 'PUT':
            response = requests.put(url, data = data, headers = headers)
        elif request_type == 'DELETE':
            response = requests.delete(url, data = data, headers = headers)

        return response
    except Exception as error:
        utils.raise_exception(error)
    
    return None
