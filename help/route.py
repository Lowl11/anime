import re

class RouteHelper:
    @staticmethod
    def module_name(path):
        result = re.findall('^\/(\w+)\/', path)
        return result[0]
