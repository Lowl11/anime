import re

"""
    route - вспомогающий класс связанный с путями (ссылками)
"""


def module_name(path):
    """ определение названия модуля """

    result = re.findall('^\/(\w+)\/', path)
    if len(result) == 0:
        return None
    return result[0]
