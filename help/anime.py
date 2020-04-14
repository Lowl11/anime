from django.conf import settings

# Подключение кастомных классов
from watch.models import Anime

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class AnimeHelper:
    @staticmethod
    def get_all():
        anime_list = Anime.objects.all()
        return anime_list
    
    @staticmethod
    def get_anime_by_id(id):
        anime = Anime.objects.get(pk = id)
        if anime is None:
            return False
        return anime
