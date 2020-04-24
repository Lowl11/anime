from django.conf import settings

# Подключение кастомных классов
from main.models import NavigationLink

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    NavigationLinksManager - вспомогательный класс являющийся инструментом для навигационных ссылок
"""
class NavigationLinksManager:
    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает все ссылки
    @staticmethod
    def get_links():
        links = NavigationLink.objects.all()
        return links

    # возвращает все ссылки отсортированные по порядковому номеру
    @staticmethod
    def get_links_by_order():
        links = NavigationLinksManager.get_links()
        sorted_links = NavigationLinksManager.sort_by_order_number(links)
        return sorted_links
    
    
    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # сортировка ссылок по порядковому номеру
    @staticmethod
    def sort_by_order_number(links):
        return sorted(links, key = lambda link: link.order_number, reverse = False)
