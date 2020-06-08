from datetime import date, datetime

from tools import debugger


def write(message, title=None):
    debugger(message, title)
    write_to_file(message, title)


def write_to_file(message, title):
    file = open('logs/' + get_logs_name(), 'a')
    file.write(prepare_message(message, title))
    file.close()


def prepare_message(message, title):
    current_time = datetime.now()
    result = '-----------------------------------'
    result += 'Дата и время: '
    result += str(current_time.day) + '-' + str(current_time.month) + '-' + str(current_time.day) + ' '
    result += str(current_time.hour) + ':' + str(current_time.min) + ':' + str(current_time.second) + '\n'
    if title is not None:
        result += '\t' + title + ':'
    result += '\t\t' + message
    result += '-----------------------------------'
    return result


def get_logs_name():
    today = date.today()
    return 'errors_' + str(today.day) + '-' + str(today.month) + '-' + str(today.year) + '.log'
