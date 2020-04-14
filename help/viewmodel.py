from django.shortcuts import render, redirect
from django.conf import settings

# Подключение кастомных классов
from .navigation_links import NavigationLinksHelper
from .genre import GenreHelper
from .route import RouteHelper
from .module import ModuleHelper

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

# Видмодель нужна чтобы не увеличивать кол-во кода при отправлении больших context'ов
# Еще при рендеринге можно добавлять настройки или проверки для каждого экшона
class ViewModel:
    __context = {}
    __path = None

    # рендеринг страницы
    def render(self, request):
        self.pre_render_settings(request)
        return render(request, self.__path, self.__context)
    
    # настройки / проверки перед рендерингом абсолютно каждой страницы
    def pre_render_settings(self, request):
        # Проверка на залогиненность юзера
        user = request.user
        if user.is_anonymous:
            self.add_object('user', None)
        else:
            self.add_object('user', user)

        # нынешний модуль в котором находится пользователь и добавление контекста модуля
        module_name = RouteHelper.module_name(request.path)
        self.add_object('module', module_name)
        self.add_module_context(module_name)

        # добавление пунктов навигационной панели
        self.add_object('navbar_links', NavigationLinksHelper.get_links_by_order())

        # добавление всех жанров аниме
        self.add_object('genre_list', GenreHelper.get_genres())
    
    # добавляет путь к HTML файлу
    def add_path(self, path):
        self.__path = path
    
    # добавляет новый объект в контекст
    def add_object(self, object_name, object):
        self.__context[object_name] = object

    # добавляет параметры контекста модуля
    def add_module_context(self, module_name):
        module_context = ModuleHelper.get_context(module_name)
        for i in range(0, module_context.size()):
            param = module_context.get(i)
            self.add_object(param.key, param.value)
        return True
