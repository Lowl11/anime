from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings

# подключение кастомных файлов
from help.viewmodel import ViewModel
from help.auth import AuthHelper
from .forms import SigninForm, SignupForm

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
    vm.add_object('form', SigninForm())
    vm.add_object('title', 'Авторизация')
    return vm.render(request)

def signin_post(request):
    AuthHelper.signin_user(request, request.POST)
    if AuthHelper.is_authorized(request):
        return redirect_home()
    return redirect_signin()

def logout_get(request):
    AuthHelper.logout(request)
    return redirect_home()

def signup_view(request):
    if AuthHelper.is_authorized(request):
        return redirect_home()

    vm = ViewModel()
    vm.add_path('a_auth/signup.html')
    vm.add_object('title', 'Регистрация пользователя')
    vm.add_object('form', SignupForm())
    return vm.render(request)

def signup_post(request):
    success = AuthHelper.signup_user(request, request.POST)
    if success:
        return redirect_signup()
    return redirect_signin()

####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################
def redirect_home():
    return redirect('/')

def redirect_signin():
    return redirect('/auth/signin/')

def redirect_signup():
    return redirect('/auth/signup/')
