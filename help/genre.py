from django.conf import settings

# Подключение кастомных классов
from watch.models import Genre

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class GenreHelper:
    @staticmethod
    def get_genres():
        genre_list = Genre.objects.all()
        return genre_list
    
