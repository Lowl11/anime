import os, shutil
from django.conf import settings

# кастомные классы
from tools import logger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

'''
    FileManager
'''


def create_folder(destination_path):
    """ создание папки на диске """
    try:
        os.mkdir(destination_path)
    finally:
        pass


def rename_folder(old, new):
    os.rename(old, new)
    logger.write('Перименование папки "' + old + '" -> "' + new + '".', logger.FILE)


def delete_folder(destination_path):
    shutil.rmtree(destination_path, ignore_errors = True)
    logger.write('Удаление папки "' + destination_path + '"', logger.FILE)


def upload_file(destination_path, file):
    pass
