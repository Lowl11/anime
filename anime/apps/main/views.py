from django.shortcuts import render, redirect
from django.conf import settings

# подключение кастомных файлов
from utils.viewmodel import ViewModel
from utils.debugger import Debugger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

def home_view(request):
    # выбираем что грузим первым
    start_from = SETTINGS['start_from']
    if start_from == 'watch':
        return redirect('/watch/')
    return not_found()

def not_found_view(request):
    vm = ViewModel()
    vm.add_path('main/notfound.html')
    vm.add_object('title', CONSTANTS['title_not_found'])
    return vm.render(request)

def xsearch_get(request):
    if request.GET:
        query = request.GET['query']
        search_type = request.GET['search_type']
        # TODO Пока что оставим так, после того как будет настроено нормальное
        # отображение страницы со списком аниме бахнем поиск
        return home_view(request)
    return not_found()


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def not_found():
    return SETTINGS['not_found_method']()
