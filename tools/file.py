import os.path

'''
    FileManager
'''

def save_file(path, file):
    full_path = os.path.join(path, file)
    file.close()

def rename_file(file, name):
    file.name = name
