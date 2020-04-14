from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

# Подключение кастомных классов
from a_auth.models import Viewer

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class AuthHelper:
    @staticmethod
    def logout(request):
        logout(request)
    
    @staticmethod
    def signin_user(request, username, password):
        base_user = authenticate(username=username, password=password)

        if base_user is not None:
            viewer = Viewer.objects.get(base_user = base_user)
            if viewer is not None:
                login(request, base_user)
        # end

    @staticmethod
    def is_authorized(request):
        if request.user.is_anonymous:
            return False
        return request.user.is_authenticated
    
