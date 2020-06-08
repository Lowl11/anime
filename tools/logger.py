from tools import debugger
from tools import utils


def write(message, title=None):
    debugger.write(message, title)
    write_to_file(message, title)


def write_to_file(message, title):
    file = open('logs/' + get_logs_name(), 'a')
    file.write(prepare_message(message, title))
    file.close()


def prepare_message(message, title):
    result = '-----------------------------------\n'
    result += 'Дата и время: '
    result += utils.today(with_time = True) + '\n'
    if title is not None:
        result += '\t' + title + ':'
    result += '\t\tТекст ошибки: ' + message
    result += '\n-----------------------------------\n\n'
    return result


def get_logs_name():
    return 'errors_' + utils.today(with_time = False) + '.log'
