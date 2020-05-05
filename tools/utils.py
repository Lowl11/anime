from django.conf import settings

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

# пытатется вернуть значение с массива по названию с реквеста
def try_get_from_request(request, type, name):
    try:
        if type == 'POST':
            return request.POST[name]
        elif type == 'GET':
            return request.GET[name]
        elif type == 'SESSION':
            return request.session[name]
        else:
            raise_exception('Данный тип не поддерживается')
    except Exception:
        raise_exception(Exception)

# пытается вернуть значение с массива по названию
def try_get_from_array(array, name):
    try:
        return array[name]
    except:
        return None
    
# вырезает пустые строки в массиве
def erase_empty_strings(array):
    result = []
    for word in array:
        if len(word) > 0:
            result.append(word)
    return result

# вызывает эксепшн если мы в режиме дебаггера
def raise_exception(exception):
    if SETTINGS['debug']:
        if type('') is type(exception):
            raise Exception(exception)
        raise exception
    # в любом случае здесь должно быть логирование
