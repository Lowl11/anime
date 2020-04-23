from django.conf import settings

# Подключение кастомных классов
from cms.models import CmsNavigationLink

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    CmsNavigationLinksHelper - вспомогательный класс являющийся инструментом для навигационных ссылок CMS
"""
class CmsNavigationLinksHelper:
    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает все ссылки
    @staticmethod
    def get_links():
        links = CmsNavigationLink.objects.all()
        return links

    # возвращает все ссылки отсортированные по порядковому номеру
    @staticmethod
    def get_links_by_order():
        links = CmsNavigationLinksHelper.get_links()
        sorted_links = CmsNavigationLinksHelper.sort_by_order_number(links)
        return sorted_links
    
    
    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # сортировка ссылок по порядковому номеру
    @staticmethod
    def sort_by_order_number(links):
        return sorted(links, key = lambda link: link.order_number, reverse = False)
