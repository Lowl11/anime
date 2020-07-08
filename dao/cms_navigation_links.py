from django.conf import settings

# Подключение кастомных классов
from cms.models import CmsNavigationLink
from dao.base import BaseDaoManager

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


class CmsNavigationLinksManager(BaseDaoManager):
    """ Вспомогательный класс являющийся инструментом для навигационных ссылок CMS """

    def __init__(self):
        preparation_method = CmsNavigationLinksManager.sort_by_order_number
        super(CmsNavigationLinksManager, self).__init__(CmsNavigationLink, preparation_method)

    # сортировка ссылок по порядковому номеру
    @staticmethod
    def sort_by_order_number(links):
        return sorted(links, key = lambda link: link.order_number, reverse = False)
