from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

# подключение кастомных файлов
from help.viewmodel import ViewModel
from help.anime import AnimeHelper
from .settings import CmsSettings
from anime.starter import Starter

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

@login_required(login_url = CONSTANTS['url_signin'])
def home_view(request):
    first_load = CmsSettings.first_load()
    if first_load == 'anime':
        return anime_view(request)
    elif first_load == 'dashboard':
        return dashboard_view(request)
    return not_found()

@login_required(login_url = CONSTANTS['url_signin'])
def anime_view(request):
    vm = ViewModel()
    vm.add_path('cms/anime.html')
    vm.add_object('title', 'Аниме')
    return vm.render(request)

@login_required(login_url = CONSTANTS['url_signin'])
def anime_manage_view(request, pk):
    vm = ViewModel()
    vm.add_path('cms/manage-anime.html')
    vm.add_object('title', 'Управление аниме')

    anime = AnimeHelper.get_anime_by_id(pk)
    if anime is None:
        return not_found()
    vm.add_object('anime', anime)
    return vm.render(request)

@login_required(login_url = CONSTANTS['url_signin'])
def dashboard_view(request):
    vm = ViewModel()
    vm.add_path('cms/dashboard.html')
    vm.add_object('title', 'Dashboard')
    return vm.render(request)


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def not_found():
    return Starter.not_found_method()
