from django.conf import settings

# Подключение кастомных классов
from utils.dict import Dictionary
from watch.forms import XSearchForm
from cms.forms import ManageAnimeForm
from utils.debugger import Debugger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

# A_AUTH Module
A_AUTH_CONTEXT = Dictionary()

# CMS Module
CMS_CONTEXT = Dictionary()

"""
    ModuleHelper - вспомогающий класс служащий инструменто помощи для работы с подулями
"""
class ModuleHelper:
    # Возвращает контекст в зависимости от названия модуля
    @staticmethod
    def get_context(module_name):
        if module_name == 'watch':
            watch_context = Dictionary()
            watch_context.add('xsearch_form', XSearchForm())
            watch_context.add('search_type', 'anime')
            return watch_context
        elif module_name == 'cms':
            return CMS_CONTEXT
        elif module_name == 'auth':
            return A_AUTH_CONTEXT
        return None
