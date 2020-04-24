from django.conf import settings

# Подключение кастомных классов
from utils.dict import Dictionary
from watch.forms import XSearchForm
from cms.forms import ManageAnimeForm
from utils import debugger
from help.cms_navigation_links import CmsNavigationLinksHelper

# A_AUTH Module
A_AUTH_CONTEXT = Dictionary()

"""
    ModuleHelper - вспомогающий класс служащий инструменто помощи для работы с подулями
"""
class ModuleHelper:
    # Возвращает контекст в зависимости от названия модуля
    @staticmethod
    def get_context(module_name):
        SETTINGS = settings.A_SETTINGS
        CONSTANTS = settings.A_CONSTANTS
        if module_name == 'watch':
            watch_context = Dictionary()
            watch_context.add('xsearch_form', XSearchForm())
            watch_context.add('anime_cover_width', CONSTANTS['anime_cover_width'])
            watch_context.add('anime_cover_height', CONSTANTS['anime_cover_height'])
            return watch_context
        elif module_name == 'cms':
            cms_context = Dictionary()
            cms_context.add('cms_navigation_links', CmsNavigationLinksHelper.get_links_by_order())
            return cms_context
        elif module_name == 'auth':
            return A_AUTH_CONTEXT
        return None
