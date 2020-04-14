"""
    Dictionary - кастомный словарь "ключ - значение".
    Приемущества:
        1. Можно обращаться отдельно к ключам
        2. Можно будет менять поведение как будет нужно
"""
class Dictionary:
    __nodes = []

    ############################# ПУБЛИЧНЫЕ МЕТОДЫ #############################
    
    # добавление новой записи
    def add(self, key, value):
        if self.check_key(key):
            self.__nodes.append(self.Node(key, value))
    
    # возвращает запись по индексу
    def get(self, index):
        return self.__nodes[index]
    
    # возвращает размер словаря
    def size(self):
        return len(self.__nodes)
    

    ############################# ПРИВАТНЫЕ МЕТОДЫ #############################

    # проверка на схожесть ключа
    def check_key(self, key):
        nodes = self.__nodes
        for node in nodes:
            if node.key == key:
                return False
        return True
    
    # перезапись метода toString()
    def __str__(self):
        result = ''
        nodes = self.__nodes
        for node in nodes:
            result += '{' + str(node.key) + ' : ' + str(node.value) + '}\n'
        return result
        
    """
        Node - POKO класс служащий для хранения ключа и значения
    """
    class Node:
        key = None
        value = None

        def __init__(self, key, value):
            self.key = key
            self.value = value
