from datetime import date, datetime

from django.conf import settings

from tools import logger

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
    except:
        # логирование
        pass
    return None

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

    logger.write(str(exception))

def today(with_time = False):
    if with_time:
        day = datetime.now()
    else:
        day = date.today()

    date_str = two_digit_number(str(day.day)) + '-' + \
               two_digit_number(str(day.month)) + '-' + str(day.year)

    if with_time:
        date_str += ' ' + two_digit_number(str(day.hour)) + \
                    ':' + two_digit_number(str(day.minute)) + \
                    ':' + two_digit_number(str(day.second))
    return date_str

def two_digit_number(num):
    str_num = str(num)
    if len(str_num) == 1:
        str_num = '0' + str_num
    return str_num
