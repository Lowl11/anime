from django.shortcuts import render, redirect
from django.conf import settings

# подключение кастомных файлов
from utils.viewmodel import ViewModel
from utils import debugger
from watch import views as watch_view

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

def home_view(request):
    # выбираем что грузим первым
    start_from = SETTINGS['main_start_from']
    if start_from == 'watch':
        return redirect('/watch/')
    return not_found()

def not_found_view(request):
    vm = ViewModel()
    vm.add_path('main/notfound.html')
    vm.add_object('title', CONSTANTS['title_not_found'])
    return vm.render(request)


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

def not_found():
    return SETTINGS['not_found_method']()
