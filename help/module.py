from django.conf import settings

# Подключение кастомных классов
from utils.dict import Dictionary
from watch.forms import XSearchForm
from cms.forms import ManageAnimeForm

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

# WATCH Module
WATCH_CONTEXT = Dictionary()
WATCH_CONTEXT.add('xsearch_form', XSearchForm())

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
            return WATCH_CONTEXT
        elif module_name == 'cms':
            return CMS_CONTEXT
        elif module_name == 'auth':
            return A_AUTH_CONTEXT
        return None
