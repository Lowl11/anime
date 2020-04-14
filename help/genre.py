from django.conf import settings

# Подключение кастомных классов
from watch.models import Genre

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    GenreHelper - вспомогающий класс
"""
class GenreHelper:
    # Возвращает все жанры аниме
    @staticmethod
    def get_genres():
        genre_list = Genre.objects.all()
        return genre_list
    
