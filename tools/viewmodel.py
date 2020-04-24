from django.shortcuts import render, redirect
from django.conf import settings

# Подключение кастомных классов
from dao.navigation_links import NavigationLinksManager
from dao.genre import GenreManager
from . import route
from . import module as ModuleManager
from tools import utils
from tools import debugger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

"""
    Видмодель - класс вызывающийся при каждом рендеринге страницы, вызывается на каждом Action методе.
    Приемущества:
        1. Видмодель нужна чтобы не увеличивать кол-во кода при отправлении больших context'ов.
        2. Еще при рендеринге можно добавлять настройки или проверки для каждого экшона.
        3. Так же можно управлять поведением от странице к странице.
"""
class ViewModel:
    def __init__(self):
        self.__context = {}
        self.__path = None
        self.__module = None


    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # рендеринг страницы
    def render(self, request):
        self.pre_render_settings(request)
        return render(request, self.__path, self.__context)
    
    # добавляет путь к HTML файлу
    def add_path(self, path):
        self.__path = path
    
    # добавляет новый объект в контекст
    def add_object(self, object_name, object):
        self.__context[object_name] = object

    
    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################
    
    # настройки / проверки перед рендерингом абсолютно каждой страницы
    def pre_render_settings(self, request):
        # Проверка на залогиненность юзера
        user = request.user
        if user.is_anonymous:
            self.add_object('user', None)
        else:
            self.add_object('user', user)
            self.add_object('role', utils.try_get_from_request(request, 'SESSION', 'role'))

        # нынешний модуль в котором находится пользователь и добавление контекста модуля
        module_name = route.module_name(request.path)
        self.__module = module_name
        self.add_object('module', module_name)
        self.add_module_context(module_name)

        # добавление пунктов навигационной панели
        self.add_object('navbar_links', NavigationLinksManager.get_links_by_order())

        # добавление всех жанров аниме
        self.add_object('genre_list', GenreManager.get_genres())

    # добавляет параметры контекста модуля
    def add_module_context(self, module_name):
        module_context = ModuleManager.get_context(module_name)
        if module_context != None:
            for i in range(0, module_context.size()):
                param = module_context.get_by_index(i)
                self.add_object(param.key, param.value)
        return True
    
    def __str__(self):
        return 'Видмодель вызванная из модуля "' + self.module + '"'
