from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date

# подключение кастомных файлов
from utils.viewmodel import ViewModel
from help.anime import AnimeHelper
from anime import starter
from .forms import ManageAnimeForm
from help.elastic import ElasticSearchHelper

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS
es_helper = SETTINGS['es_helper']


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

@login_required(login_url = CONSTANTS['url_signin'])
def home_view(request):
    # выбираем что грузим первым
    start_from = SETTINGS['cms_start_from']
    if start_from == 'anime':
        return anime_view(request)
    elif start_from == 'dashboard':
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

    vm.add_object('manage_anime_form', AnimeHelper.fill_form(ManageAnimeForm(), anime))
    vm.add_object('anime_id', pk)
    return vm.render(request)

@login_required(login_url = CONSTANTS['url_signin'])
def dashboard_view(request):
    vm = ViewModel()
    vm.add_path('cms/dashboard.html')
    vm.add_object('title', 'Dashboard')
    return vm.render(request)

@login_required(login_url = CONSTANTS['url_signin'])
def elastic_view(request):
    vm = ViewModel()
    vm.add_path('cms/elastic.html')
    vm.add_object('title', 'ElasticSearch')
    vm.add_object('indices', es_helper.get_all_indices())
    return vm.render(request)


def elastic_delete_index_get(request, index_name):
    if es_helper.delete_index(index_name):
        return redirect_elastic()
    return not_found()

def elastic_fill_get(request, data_type):
    today = date.today().strftime('%d.%m.%Y')
    if es_helper.create_index(data_type + '-' + today) == False:
        return not_found()
    return redirect_elastic()

####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def not_found():
    return starter.not_found_method()

def redirect_elastic():
    return redirect('/cms/elastic/')
