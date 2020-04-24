import re

"""
    route - вспомогающий класс связанный с путями (ссылками)
"""

# определение названия модуля
def module_name(path):
    result = re.findall('^\/(\w+)\/', path)
    if len(result) == 0:
        return None
    return result[0]
