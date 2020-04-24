from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

# Подключение кастомных классов
from a_auth.models import Viewer, Role

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    AuthManager - инструмент для авторизации, регистрации и выхода
"""
class AuthManager:
    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # выход из аккаунта
    @staticmethod
    def logout(request):
        logout(request)

    # авторизация пользователя
    @staticmethod
    def signin_user(request, dict):
        # проверяем есть ли пользователь с такими данными
        base_user = authenticate(username = dict['username'], password = dict['password'])

        if base_user is not None:
            viewer = Viewer.objects.get(base_user = base_user)
            if viewer is not None:
                # авторизуем пользователя
                login(request, base_user)
                viewer = Viewer.objects.get(base_user = base_user)
                request.session['role'] = viewer.role.value
        # end
    
    # регистрация пользователя
    @staticmethod
    def signup_user(request, dict):
        username = dict['username']
        password = dict['password']
        re_password = dict['re_password']
        first_name = dict['first_name']
        last_name = dict['last_name']

        if password == re_password:
            try:
                viewer = Viewer()
                viewer.signup_base_user(username, password, first_name, last_name)
                viewer.role = AuthManager.default_role()
                viewer.save()
            except:
                return False
        return True

    # проверка авторизован ли пользователь
    @staticmethod
    def is_authorized(request):
        if request.user.is_anonymous:
            return False
        return request.user.is_authenticated
    
    
    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает роль пользователя по умолчанию
    @staticmethod
    def default_role():
        return Role.objects.get(value = 3)
    
