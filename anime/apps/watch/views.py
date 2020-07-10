from django.shortcuts import HttpResponse
from django.conf import settings
from datetime import datetime
import json
import pytz

# подключение кастомных файлов
from dao.anime import AnimeManager
from dao.anime_comments import AnimeCommentsManager
from dao.auth import AuthManager
from tools.viewmodel import ViewModel
from tools.elastic.manager import ElasticSearchManager
from tools import utils, debugger, logger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS
es_manager = ElasticSearchManager()
anime_manager = AnimeManager()
auth_manager = AuthManager()


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

# Отображение списка аниме
def page_view(request):
    title = 'Смотреть аниме'
    return display_anime_list(request, anime_manager.get_all(), title)


# Отображение одного аниме
def anime_view(request, pk):
    anime = anime_manager.get_by_id(pk)
    if not anime:
        return not_found()

    vm = ViewModel()
    vm.add_path('watch/anime.html')
    vm.add_object('title', 'Смотреть аниме "' + str(anime) + '"')
    vm.add_object('anime', anime)
    vm.add_object('comments', AnimeCommentsManager.get_all(anime))
    return vm.render(request)


def comment_post(request):
    if request.POST:
        anime_id = utils.try_get_from_request(request, utils.POST, 'anime_id')
        text = utils.try_get_from_request(request, utils.POST, 'text')

        author = auth_manager.get_by_id(request.session['viewer_id'])
        anime = anime_manager.get_by_id(anime_id)
        if author is None or anime is None:
            logger.write('В методе comment_post() отсутствует author или anime. Author = ' + str(author) + ' | '
                         + str(anime), logger.DAO)
            code = 0
            return HttpResponse(code)
        comment = AnimeCommentsManager.create(author, anime, text)

        publish_date = comment.publish_date.astimezone(pytz.timezone("Asia/Almaty")).strftime("%d %B %Y %H:%M")

        obj = {
            'id': comment.id,
            'author': {
                'id': str(comment.author.id),
                'image_url': str(comment.author.image.url),
                'username': str(comment.author.base_user.username),
                'role': str(comment.author.role.value)
            },
            'publish_date': str(publish_date),
            'text': comment.text
        }
        comment_json = json.dumps(obj)
        return HttpResponse(comment_json, content_type='application/json')
    code = 0
    return HttpResponse(code)


def delete_comment_post(request):
    code = 1
    if request.POST:
        comment_id = utils.try_get_from_request(request, utils.POST, 'id')
        if not AnimeCommentsManager.delete(comment_id):
            code = 0
        return HttpResponse(code)
    code = 0
    return HttpResponse(code)


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

    query = utils.try_get_from_request(request, utils.GET, 'query')
    if query is not None:
        vm.add_object('query', query)
    return vm.render(request)


def not_found():
    return SETTINGS['not_found_method']()
