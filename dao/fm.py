from django.conf import settings

# кастомные классы
from cms.models import File, Folder
from tools import file
from tools import debugger

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

class FileManager:
    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    # возвращает объекты под родительским объектом
    @staticmethod
    def get_objects(parent):
        folders = Folder.objects.filter(parent = parent).order_by('folder__name')
        for folder in folders:
            folder.type = 'folder'
        return folders
    
    # возвращает объекты под родительским объектом в виде массива (а не QuerySet)
    @staticmethod
    def get_objects_array(parent):
        objects = FileManager.get_objects(parent)
        array = []
        for obj in objects:
            assosiative = {}
            assosiative['id'] = obj.id
            assosiative['name'] = obj.name
            if obj.parent is not None:
                assosiative['parent'] = obj.parent.id
            else:
                assosiative['parent'] = None
            assosiative['type'] = obj.type
            array.append(assosiative)
        return array

    # возвращает папку по id
    @staticmethod
    def get_folder_by_id(id):
        try:    
            return Folder.objects.get(pk = id)
        except:
            pass
        return None
    
    # возвращает файл по id
    @staticmethod
    def get_file_by_id(id):
        try:
            return File.objects.get(pk = id)
        except:
            pass
        return None
    
    # создание папки в БД и на диске
    @staticmethod
    def create_folder(parent_id, folder_name):
        # сохраняем папку в БД
        parent = None # root

        if parent != 0: # если ID не 0 то значит не root
            parent = FileManager.get_folder_by_id(parent_id)
        
        if FileManager.check_folder(parent, folder_name):
            folder = Folder()
            folder.name = folder_name
            folder.parent = parent
            folder.save()

            # потом создаем папку на диске
            destination_path = SETTINGS['media_root']
            destination_path += FileManager.build_path(parent, folder_name)
            file.create_folder(destination_path)
    
    # редактирование названия папки
    @staticmethod
    def rename_folder(folder_id, folder_name):
        folder = FileManager.get_folder_by_id(folder_id)
        if folder is not None:
            old_name = folder.name
            folder.name = folder_name
            folder.save()

            # переименовываем папку на диске
            old_path = SETTINGS['media_root']
            new_path = SETTINGS['media_root']

            old_path += FileManager.build_path(folder.parent, old_name)
            new_path += FileManager.build_path(folder.parent, folder_name)

            file.rename_folder(old_path, new_path)


    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################
    
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
            parent = parent.parent
        return '/' + path
