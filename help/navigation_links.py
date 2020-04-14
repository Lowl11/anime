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
