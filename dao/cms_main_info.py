from django.conf import settings
from django.utils import timezone
from datetime import datetime

# Подключение кастомных классов
from cms.models import CmsMainInfo
from tools.dict import Dictionary
from tools import forms as FormManager
from tools import debugger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class CmsMainInfoManager:
    @staticmethod
    def get_notifications():
        # TODO: не хардкодить цифру 1 (primary key)
        main_info = CmsMainInfo.objects.get(pk = 1)
        notifications = {}
        notifications['main'] = main_info.main_notification
        notifications['mini1'] = main_info.mini_notification1
        notifications['mini2'] = main_info.mini_notification2
        return notifications
