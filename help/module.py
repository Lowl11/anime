from django.conf import settings

# Подключение кастомных классов
from watch.forms import XSearchForm
from utils.dict import Dictionary

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


# WATCH Module
WATCH_CONTEXT = Dictionary()
WATCH_CONTEXT.add('xsearch_form', XSearchForm())

# ModuleHelper
class ModuleHelper:
    @staticmethod
    def get_context(module_name):
        if module_name == 'watch':
            return WATCH_CONTEXT
        return None
