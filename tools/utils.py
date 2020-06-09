from datetime import date, datetime
from django.conf import settings

from tools import logger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

POST = 'POST'
GET = 'GET'
SESSION = 'SESSION'


# пытатется вернуть значение с массива по названию с реквеста
def try_get_from_request(request, request_type, name):
    try:
        if request_type == POST:
            return request.POST[name]
        elif request_type == GET:
            return request.GET[name]
        elif request_type == SESSION:
            return request.session[name]
        else:
            logger.write('Тип ' + request_type + ' не поддерживается', logger.HTTP)
    except Exception as error:
        logger.write('Неизвестная ошибка: ' + str(error), logger.HTTP)
    return None


# пытается вернуть значение с массива по названию
def try_get_from_array(array, name):
    try:
        return array[name]
    finally:
        return None


# вырезает пустые строки в массиве
def erase_empty_strings(array):
    result = []
    for word in array:
        if len(word) > 0:
            result.append(word)
    return result


# вызывает эксепшн если мы в режиме дебаггера
def raise_exception(exception, logger_type):
    if SETTINGS['debug']:
        if type('') is type(exception):
            raise Exception(exception)
        raise exception

    logger.write(str(exception), logger_type)


def today(with_time=False):
    if with_time:
        day = datetime.now()
    else:
        day = date.today()

    date_str = two_digit_number(str(day.day)) + '-' + two_digit_number(str(day.month)) + '-' + str(day.year)

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
