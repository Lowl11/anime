from django.shortcuts import render, redirect
from django.conf import settings

# подключение кастомных файлов
from utils.viewmodel import ViewModel
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
def genre_view(request, name):
    title = 'Аниме по жанру "' + name + '"'
    return display_anime_list(request, AnimeHelper.get_by_genre(name), title)

# отображение аниме по году
def year_view(request, year):
    title = 'Аниме по году "' + str(year) + '"'
    return display_anime_list(request, AnimeHelper.get_by_year(year), title)


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def display_anime_list(request, anime_list, title):
    vm = ViewModel()
    vm.add_path('watch/page.html')
    vm.add_object('title', title)
    vm.add_object('anime_list', anime_list)
    return vm.render(request)

def not_found():
    return SETTINGS['not_found_method']()
