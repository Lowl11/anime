from django.shortcuts import render, redirect
from django.conf import settings

A_SETTINGS = settings.A_SETTINGS

# Видмодель нужна чтобы не увеличивать кол-во кода при отправлении больших context'ов
# Еще при рендеринге можно добавлять настройки или проверки для каждого экшона
class ViewModel:
    __context = {}
    __path = None

    # рендеринг страницы
    def render(self, request):
        return render(request, self.__path, self.__context)
    
    # настройки / проверки перед рендерингом абсолютно каждой страницы
    def pre_render_settings(request):
        # Проверка на залогиненность юзера
        user = request.user
        if user is not None:
            self.add_object('user', user)
        
        # Проверка на необходимость прогружать прелоадер
        self.add_object('preloader', A_SETTINGS['preloader'])
    
    # добавляет путь к HTML файлу
    def add_path(self, path):
        self.__path = path
    
    # добавляет новый объект в контекст
    def add_object(self, object_name, object):
        self.__context[object_name] = object
    
