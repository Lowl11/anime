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
def page_view(request):
    title = 'Смотреть аниме'
    return display_anime_list(request, AnimeHelper.get_all(), title)


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


# поиск аниме
def xsearch_get(request):
    if request.GET:
        query = request.GET['query']
        anime_list = AnimeHelper.search(query.lower())
        result_quantity = len(anime_list)
        title = 'Поиск по запросу "' + query + '" выдал ' + str(result_quantity) + ' результат(ов)'
        return display_anime_list(request, anime_list, title)
    return not_found()

####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

# метод отображения списка аниме
def display_anime_list(request, anime_list, title):
    vm = ViewModel()
    vm.add_path('watch/page.html')
    vm.add_object('title', title)
    vm.add_object('anime_list', anime_list)
    return vm.render(request)

def not_found():
    return SETTINGS['not_found_method']()
