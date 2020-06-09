import requests

""" REST - тулза которая помогает отправить запрос по урлу """


def make_request(url, data, request_type, headers=None):
    """ делает запрос по урлу """
    if headers is None:  # по дефолту будем отправлять JSON
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    response = None
    err = None
    # try/except потому что нужно будет отловить ошибку и логировать (или выкинуть)
    try:

        if request_type == 'POST':
            response = requests.post(url, data=data, headers=headers)
        elif request_type == 'GET':
            response = requests.get(url, data=data, headers=headers)
        elif request_type == 'PUT':
            response = requests.put(url, data=data, headers=headers)
        elif request_type == 'DELETE':
            response = requests.delete(url, data=data, headers=headers)

    except Exception as error:
        err = error

    response.close()

    return response, err
