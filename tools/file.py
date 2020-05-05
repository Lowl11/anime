import os
from django.conf import settings

# кастомные классы
from tools import debugger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

'''
    FileManager
'''

# создание папки на диске
def create_folder(destination_path, folder_name):
    media_folder = SETTINGS['media_root']
    media_folder += destination_path
    media_folder += folder_name

    try:
        os.mkdir(media_folder)
    except:
        pass
