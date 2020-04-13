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
# Create your views here.
def page_view(reqeust):
    vm = ViewModel()
    vm.add_path('watch/page.html')
    vm.add_object('title', CONSTANTS['title_watch_home_view'])
    vm.add_object('anime_list', AnimeHelper.get_all())
    vm.add_object('anime_cover_width', CONSTANTS['anime_cover_width'])
    vm.add_object('anime_cover_height', CONSTANTS['anime_cover_height'])
    return vm.render(reqeust)


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################
def some_private_method():
    pass
