from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class AuthHelper:
    @staticmethod
    def logout(request):
        logout(request)

    @staticmethod
    def is_authorized(request):
        if request.user.is_anonymous:
            return False
        return request.user.is_authenticated
    
