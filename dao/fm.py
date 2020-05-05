from cms.models import File, Folder
from tools import file

class FileManager:
    @staticmethod
    def get_root_objects():
        folders = Folder.objects.all()
        for folder in folders:
            folder.type = 'folder'
        return folders
    
    # создание папки в БД и на диске
    @staticmethod
    def create_folder(previous_path, folder_name):
        # сохраняем папку в БД
        folder = Folder()
        folder.name = folder_name
        folder.parent = previous_path
        folder.save()

        # потом создаем папку на диске
        destination_path = '/'
        file.create_folder(destination_path, folder_name)
    
    # проверка папки (можно ли создавать)
    @staticmethod
    def check_folder(path, folder_name):
        folders = Folder.objects.all()
        folders_with_same_name = folders.filter(name__equals = folder_name)
        return True
    
    # построение пути на основе папок в БД
    @staticmethod
    def build_path(folder):
        path = ''
        while True:
            path += folder.name
            parent = folder.parent
            if parent is None:
                break
        return path
