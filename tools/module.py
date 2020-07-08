from django.conf import settings

# Подключение кастомных классов
from tools.dict import Dictionary
from watch.forms import XSearchForm
from cms.forms import ManageAnimeForm
from tools import logger
from dao.cms_navigation_links import CmsNavigationLinksManager
from dao.cms_main_info import CmsMainInfoManager

"""
    ModuleHelper - вспомогающий класс служащий инструменто помощи для работы с подулями
"""

cms_navigation_links_manager = CmsNavigationLinksManager()


def get_context(module_name):
    """" Возвращает контекст в зависимости от названия модуля """

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
        cms_context.add('cms_navigation_links', cms_navigation_links_manager.get_all())
        cms_context.add('notifications', CmsMainInfoManager.get_notifications())
        return cms_context
    elif module_name == 'auth':
        auth_context = Dictionary()
        return auth_context
    elif module_name == 'feedback':
        feedback_context = Dictionary()
        return feedback_context
    else:
        if module_name is None:
            logger.write('Был произведен запрос в безмодульный режим', logger.MODULE)
        else:
            logger.write('Модуля "' + module_name + '" нет', logger.MODULE)
    return None
