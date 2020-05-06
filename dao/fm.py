from django.conf import settings

# кастомные классы
from cms.models import File, Folder
from tools import file
from tools import debugger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class FileManager:
    @staticmethod
    def get_root_objects():
        folders = Folder.objects.filter(parent = None) # содержимое root
        for folder in folders:
            folder.type = 'folder'
        return folders

    @staticmethod
    def get_by_id(id):
        try:    
            return Folder.objects.get(pk = id)
        except:
            pass
        return None
    
    # создание папки в БД и на диске
    @staticmethod
    def create_folder(parent_id, folder_name):
        # сохраняем папку в БД
        parent = None # root

        if parent != 0: # если ID не 0 то значит не root
            parent = FileManager.get_by_id(parent_id)
        
        if FileManager.check_folder(parent, folder_name):
            folder = Folder()
            folder.name = folder_name
            folder.parent = parent
            folder.save()

            # потом создаем папку на диске
            destination_path = SETTINGS['media_root']
            destination_path += FileManager.build_path(parent, folder_name)
            file.create_folder(destination_path)
    
    # проверка папки (можно ли создавать)
    @staticmethod
    def check_folder(parent, folder_name):
        folders = Folder.objects.filter(parent = parent)
        for folder in folders:
            if folder.name == folder_name:
                return False
        return True
    
    # построение пути на основе папок в БД
    @staticmethod
    def build_path(parent, folder_name):
        path = folder_name
        while parent is not None:
            path = parent.name + '/' + path
        return path
