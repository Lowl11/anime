import os, shutil
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

def delete_folder(destination_path):
    shutil.rmtree(destination_path, ignore_errors = True)

def upload_file(destination_path, file):
    pass
