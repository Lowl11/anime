import re

"""
    RouteHelper - вспомогающий класс связанный с путями (ссылками)
"""
class RouteHelper:
    # возвращает наименование модуля в зависимости от URL'а
    @staticmethod
    def module_name(path):
        result = re.findall('^\/(\w+)\/', path)
        if len(result) == 0:
            return None
        return result[0]
