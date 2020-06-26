from django.shortcuts import render, redirect
from django.conf import settings

# подключение кастомных файлов
from tools.viewmodel import ViewModel
from dao.anime import AnimeManager
from dao.anime_comments import AnimeCommentsManager
from tools.elastic.manager import ElasticSearchManager

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS
es_manager = ElasticSearchManager()


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

# Отображение списка аниме
def page_view(request):
    title = 'Смотреть аниме'
    return display_anime_list(request, AnimeManager.get_all(), title)


# Отображение одного аниме
def anime_view(reqeust, pk):
    anime = AnimeManager.get_anime_by_id(pk)
    if not anime:
        return not_found()

    vm = ViewModel()
    vm.add_path('watch/anime.html')
    vm.add_object('title', 'Смотреть аниме "' + str(anime) + '"')
    vm.add_object('anime', anime)
    vm.add_object('comments', AnimeCommentsManager.get_all(anime))
    return vm.render(reqeust)


# отображение аниме принадлежащие определенному жанру
def genre_view(request, name):
    title = 'Аниме по жанру "' + name + '"'
    return display_anime_list(request, AnimeManager.get_by_genre(name), title)


# отображение аниме по году
def year_view(request, year):
    title = 'Аниме по году "' + str(year) + '"'
    return display_anime_list(request, AnimeManager.get_by_year(year), title)


# поиск аниме
def xsearch_get(request):
    if request.GET:
        query = request.GET['query']
        if len(query) < 4:
            return not_found()
        anime_list = es_manager.search_anime(query)
        no_image = True
        if anime_list is None:
            no_image = False
            anime_list = AnimeManager.search(query.lower())
        result_quantity = len(anime_list)
        title = 'Поиск по запросу "' + query + '" выдал ' + str(result_quantity) + ' результат(ов)'
        return display_anime_list(request, anime_list, title, no_image)
    return not_found()


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

# метод отображения списка аниме
def display_anime_list(request, anime_list, title, no_image=False):
    vm = ViewModel()
    vm.add_path('watch/page.html')
    vm.add_object('title', title)
    vm.add_object('anime_list', anime_list)
    vm.add_object('no_image', no_image)
    return vm.render(request)


def not_found():
    return SETTINGS['not_found_method']()
