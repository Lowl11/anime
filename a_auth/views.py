from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings

# подключение кастомных файлов
from help.viewmodel import ViewModel
from help.auth import AuthHelper

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################
def signin_view(request):
    # если пользователь залогинен, то на страницу с формой входа запрещен
    if AuthHelper.is_authorized(request):
        return redirect_home()
    
    vm = ViewModel()
    vm.add_path('a_auth/signin.html')
    return vm.render(request)

def logout_get(request):
    AuthHelper.logout(request)
    return redirect_home()

def signup_view(request):
    vm = ViewModel()
    vm.add_path('a_auth/signup.html')
    return vm.render(request)

####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################
def redirect_home():
    return redirect('/')