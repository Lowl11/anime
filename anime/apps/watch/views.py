from django.shortcuts import render, redirect
from django.conf import settings

# подключение кастомных файлов
from help.viewmodel import ViewModel
from help.anime import AnimeHelper

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

# Отображение списка аниме
def page_view(reqeust):
    vm = ViewModel()
    vm.add_path('watch/page.html')
    vm.add_object('title', CONSTANTS['title_watch_home_view'])
    vm.add_object('anime_list', AnimeHelper.get_all())
    vm.add_object('anime_cover_width', CONSTANTS['anime_cover_width'])
    vm.add_object('anime_cover_height', CONSTANTS['anime_cover_height'])
    return vm.render(reqeust)


# Отображение одного аниме
def anime_view(reqeust, pk):
    anime = AnimeHelper.get_anime_by_id(pk)
    if anime == False:
        return not_found()
    
    vm = ViewModel()
    vm.add_path('watch/anime.html')
    vm.add_object('title', 'Смотреть аниме "' + str(anime) + '"')
    vm.add_object('anime', anime)
    return vm.render(reqeust)

# отображение аниме принадлежащие определенному жанру
def genre_view(reqeust, name):
    vm = ViewModel()
    vm.add_path('watch/page.html')
    vm.add_object('title', 'Аниме по жанру "' + name + '"')
    vm.add_object('anime_list', AnimeHelper.get_by_genre(name))
    return vm.render(reqeust)


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def not_found():
    return SETTINGS['not_found_method']()
