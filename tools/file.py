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
def create_folder(destination_path):
    try:
        os.mkdir(destination_path)
    except:
        pass

def rename_folder(old, new):
    os.rename(old, new)
