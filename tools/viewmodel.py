from django.conf import settings
from django.shortcuts import render

# Подключение кастомных классов
from dao.genre import GenreManager
from dao.navigation_links import NavigationLinksManager
from tools import utils
from . import module as ModuleManager
from . import route

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


class ViewModel:
    """ Видмодель - класс вызывающийся при каждом рендеринге страницы, вызывается на каждом Action методе """

    def __init__(self):
        self.__context = {}
        self.__path = None
        self.__module = None

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def render(self, request):
        """ рендеринг страницы """

        self.pre_render_settings(request)
        return render(request, self.__path, self.__context)

    def add_path(self, path):
        """ добавляет путь к HTML файлу """
        self.__path = path

    def add_object(self, object_name, object):
        """ добавляет новый объект в контекст """
        self.__context[object_name] = object

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def pre_render_settings(self, request):
        """ настройки / проверки перед рендерингом абсолютно каждой страницы """

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

    def add_module_context(self, module_name):
        """ добавляет параметры контекста модуля """
        module_context = ModuleManager.get_context(module_name)
        if module_context is not None:
            for i in range(0, module_context.size()):
                param = module_context.get_by_index(i)
                self.add_object(param.key, param.value)
        return True

    def __str__(self):
        return 'Видмодель вызванная из модуля "' + self.module + '"'
