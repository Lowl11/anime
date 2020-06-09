from django.conf import settings
from django.shortcuts import redirect

from dao.auth import AuthManager
from tools import utils as UtilsHelper
# подключение кастомных файлов
from tools.viewmodel import ViewModel
from .forms import SigninForm, SignupForm

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


####################################################################
######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
####################################################################

def signin_view(request):
    # если пользователь залогинен, то на страницу с формой входа запрещен
    if AuthManager.is_authorized(request):
        return redirect_home()

    vm = ViewModel()
    vm.add_path('a_auth/signin.html')
    vm.add_object('form', SigninForm())
    vm.add_object('title', 'Авторизация')
    vm.add_object('next', UtilsHelper.try_get_from_request(request, 'GET', 'next'))
    return vm.render(request)


def signin_post(request):
    AuthManager.signin_user(request, request.POST)

    if AuthManager.is_authorized(request):
        return prepare_post(request)
    return redirect_signin()


def logout_get(request):
    AuthManager.logout(request)
    return redirect_home()


def signup_view(request):
    if AuthManager.is_authorized(request):
        return redirect_home()

    vm = ViewModel()
    vm.add_path('a_auth/signup.html')
    vm.add_object('title', 'Регистрация пользователя')
    vm.add_object('form', SignupForm())
    return vm.render(request)


def signup_post(request):
    success = AuthManager.signup_user(request, request.POST)
    if success:
        return redirect_signup()
    return redirect_signin()


####################################################################
######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
####################################################################

# подготовка реквеста после обработки POST запроса
def prepare_post(request):
    if request.POST:
        # проверка на следующий URL
        next_value = UtilsHelper.try_get_from_request(request, 'POST', 'next')
        if next_value is None:
            return redirect(next_value)
    return redirect_home()


def redirect_home():
    return redirect('/')


def redirect_signin():
    return redirect('/auth/signin/')


def redirect_signup():
    return redirect('/auth/signup/')
