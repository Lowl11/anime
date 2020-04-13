from django.shortcuts import render, redirect
from django.conf import settings

# подключение кастомных файлов
from help.viewmodel import ViewModel

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
    return vm.render(reqeust)


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################
def some_private_method():
    pass
