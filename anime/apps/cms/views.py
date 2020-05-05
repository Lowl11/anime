from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date

# подключение кастомных файлов
from tools.viewmodel import ViewModel
from dao.anime import AnimeManager
from dao.fm import FileManager
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
    vm.add_object('anime_list', AnimeManager.get_all())
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

@login_required(login_url = CONSTANTS['url_signin'])
def fm_view(request):
    vm = ViewModel()
    vm.add_path('cms/fm.html')
    vm.add_object('title', 'Файловый менеджер')
    return vm.render(request)


######################## Manage Anime ##########################

def manage_anime_post(request):
    if request.POST:
        action = utils.try_get_from_request(request, 'POST', 'action')
        if action == 'create':
            create_anime(request)
        elif action == 'edit':
            edit_anime(request)
        else:
            utils.raise_exception('Не существующее действие (CMS - views - manage_anime_post)')
    return redirect_manage_anime(anime_id)

@login_required(login_url = CONSTANTS['url_signin'])
def anime_new_view(request):
    vm = ViewModel()
    vm.add_path('cms/manage-anime.html')
    vm.add_object('title', 'Новое аниме')
    vm.add_object('manage_anime_form', ManageAnimeForm())
    vm.add_object('action', 'create')
    return vm.render(request)

@login_required(login_url = CONSTANTS['url_signin'])
def manage_anime_view(request, pk):
    vm = ViewModel()
    vm.add_path('cms/manage-anime.html')
    vm.add_object('title', 'Редактирование аниме')

    anime = AnimeManager.get_anime_by_id(pk)
    if anime is None:
        return not_found()
    vm.add_object('anime', anime)

    vm.add_object('manage_anime_form', AnimeManager.fill_form(ManageAnimeForm(), anime))
    vm.add_object('anime_id', pk)
    vm.add_object('action', 'edit')
    return vm.render(request)


######################## ElasticSearch ##########################

def elastic_delete_index_ajax(request, index_name):
    if es_manager.delete_index(index_name):
        return redirect_elastic()
    return not_found()

def elastic_fill_get(request, data_type):
    es_manager.create_index(data_type)
    es_manager.fill_index(data_type)
    
    return redirect_elastic()


######################## FileManager ##########################

def fm_create_folder_get(request):
    if request.GET:
        folder_name = utils.try_get_from_request(request, 'GET', 'name')
        previous_path = utils.try_get_from_request(request, 'GET', 'path')
        FileManager.create_folder(previous_path, folder_name)
    return HttpResponse('true')


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def create_anime(request):
    created = Dictionary()
    created.add('title_rus', utils.try_get_from_request(request, 'POST', 'title_rus'))
    created.add('title_foreign', utils.try_get_from_request(request, 'POST', 'title_foreign'))
    created.add('episodes_quantity', utils.try_get_from_request(request, 'POST', 'episodes_quantity'))
    created.add('season', utils.try_get_from_request(request, 'POST', 'season'))
    created.add('start_date', utils.try_get_from_request(request, 'POST', 'start_date'))
    created.add('description', utils.try_get_from_request(request, 'POST', 'description'))

    image = utils.try_get_from_request(request, 'POST', 'image')
    debugger.write(image)

    created.clear_from_empty()

def edit_anime(request):
    updated = Dictionary()
    updated.add('title_rus', utils.try_get_from_request(request, 'POST', 'title_rus'))
    updated.add('title_foreign', utils.try_get_from_request(request, 'POST', 'title_foreign'))
    updated.add('episodes_quantity', utils.try_get_from_request(request, 'POST', 'episodes_quantity'))
    updated.add('season', utils.try_get_from_request(request, 'POST', 'season'))
    updated.add('start_date', utils.try_get_from_request(request, 'POST', 'start_date'))
    updated.add('description', utils.try_get_from_request(request, 'POST', 'description'))
    updated.clear_from_empty()

    anime_id = request.try_get_from_request(request, 'POST', 'anime_id')
    AnimeManager.update_anime_by_id(anime_id, updated.to_assosiative())

def not_found():
    return starter.not_found_method()

def redirect_elastic():
    return redirect('/cms/elastic/')

def redirect_manage_anime(anime_id):
    return redirect('/cms/anime/manage/' + str(anime_id))
