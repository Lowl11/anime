from django.conf import settings

# Подключение кастомных классов
from main.models import NavigationLink

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class NavigationLinksHelper:
    @staticmethod
    def get_links():
        links = NavigationLink.objects.all()
        return links

    @staticmethod
    def get_links_by_order():
        links = NavigationLinksHelper.get_links()
        sorted_links = NavigationLinksHelper.sort_by_order_number(links)
        return sorted_links
    
    @staticmethod
    def sort_by_order_number(links):
        return sorted(links, key = lambda link: link.order_number, reverse = False)
