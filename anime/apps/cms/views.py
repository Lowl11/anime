from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date

# подключение кастомных файлов
from tools.viewmodel import ViewModel
from dao.anime import AnimeManager
from tools.elastic.manager import ElasticSearchManager
from anime import starter
from .forms import ManageAnimeForm
from tools import debugger
from tools.dict import Dictionary
from tools import utils

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS
es_manager = ElasticSearchManager()


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
def manage_anime_view(request, pk):
    vm = ViewModel()
    vm.add_path('cms/manage-anime.html')
    vm.add_object('title', 'Управление аниме')

    anime = AnimeManager.get_anime_by_id(pk)
    if anime is None:
        return not_found()
    vm.add_object('anime', anime)

    vm.add_object('manage_anime_form', AnimeManager.fill_form(ManageAnimeForm(), anime))
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
    vm.add_object('indices', es_manager.get_all_indices())
    return vm.render(request)


######################## Manage Anime ##########################

def manage_anime_post(request):
    if request.POST:
        updated = Dictionary()
        anime_id = request.POST['anime_id']

        updated.add('title_rus', utils.try_get_from_request(request, 'POST', 'title_rus'))
        updated.add('title_foreign', utils.try_get_from_request(request, 'POST', 'title_foreign'))
        updated.add('episodes_quantity', utils.try_get_from_request(request, 'POST', 'episodes_quantity'))
        updated.add('season', utils.try_get_from_request(request, 'POST', 'season'))
        updated.add('start_date', utils.try_get_from_request(request, 'POST', 'start_date'))
        updated.add('description', utils.try_get_from_request(request, 'POST', 'description'))
        updated.clear_from_empty()

        result = AnimeManager.update_anime_by_id(anime_id, updated.to_assosiative())
    return redirect_manage_anime(anime_id)


######################## ElasticSearch ##########################

def elastic_delete_index_ajax(request, index_name):
    if es_manager.delete_index(index_name):
        return redirect_elastic()
    return not_found()

def elastic_fill_get(request, data_type):
    es_manager.create_index('anime')
    es_manager.fill_index_by_anime()
    
    return redirect_elastic()


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def not_found():
    return starter.not_found_method()

def redirect_elastic():
    return redirect('/cms/elastic/')

def redirect_manage_anime(anime_id):
    return redirect('/cms/anime/manage/' + str(anime_id))
