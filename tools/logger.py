import textwrap

from tools import debugger
from tools import utils


HTTP = 1
ELASTIC = 2


def write(message, type):
    title, file_name = define(type)
    debugger.write(message, title)
    write_to_file(message, title, file_name)


def write_to_file(message, title, file_name):
    file = open('logs/' + get_logs_name(file_name), 'a')
    file.write(prepare_message(message, title))
    file.close()


def prepare_message(message, title):
    result = '-----------------------------------\n'
    result += 'Дата и время: '
    result += utils.today(with_time = True) + '\n'
    if title is not None:
        result += '\t\t*** ' + title + ' ***\n'
    result += '\t\tОписание:\n' + beautify_message(message)
    result += '\n-----------------------------------\n\n'
    return result


def beautify_message(message):
    return textwrap.fill(message, 100)


def define(logger_type):
    if logger_type == HTTP:
        title = 'HTTP запрос'
        file_name = 'http'
    elif logger_type == ELASTIC:
        title = 'ElasticSearch'
        file_name = 'elastic'
    else:
        title = 'Неизвестная запись'
        file_name = 'unknown'
    return title, file_name


def get_logs_name(file_name):
    return file_name + '_' + utils.today(with_time = False) + '.log'
