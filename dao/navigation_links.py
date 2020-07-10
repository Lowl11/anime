from django.conf import settings

# Подключение кастомных классов
from main.models import NavigationLink
from .base import BaseDaoManager

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


class NavigationLinksManager(BaseDaoManager):
    """ Вспомогательный класс являющийся инструментом для навигационных ссылок """

    def __init__(self):
        preparation_method = NavigationLinksManager.sort_by_order_number
        super(NavigationLinksManager, self).__init__(NavigationLink, preparation_method)

    # сортировка ссылок по порядковому номеру
    @staticmethod
    def sort_by_order_number(links):
        return sorted(links, key = lambda link: link.order_number, reverse = False)
