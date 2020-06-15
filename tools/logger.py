import textwrap

from tools import debugger
from tools import utils


HTTP = 1
ELASTIC = 2
AUTH = 3
MODULE = 4
FILE = 5
TASK = 6


def write(message, logger_type):
    title, file_name = define(logger_type)
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
    return textwrap.fill(str(message), 100)


def define(logger_type):
    if logger_type == HTTP:
        title = 'HTTP запрос'
        file_name = 'http'
    elif logger_type == ELASTIC:
        title = 'ElasticSearch'
        file_name = 'elastic'
    elif logger_type == AUTH:
        title = 'Authentication'
        file_name = 'auth'
    elif logger_type == MODULE:
        title = 'Module/App'
        file_name = 'module'
    elif logger_type == FILE:
        title = 'Файловая система'
        file_name = 'file'
    elif logger_type == TASK:
        title = 'Tasks/Jobs'
        file_name = 'tasks'
    else:
        title = 'Неизвестная запись'
        file_name = 'unknown'
    return title, file_name


def get_logs_name(file_name):
    return file_name + '_' + utils.today(with_time = False) + '.log'
