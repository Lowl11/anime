"""
    Dictionary - кастомный словарь "ключ - значение".
    Приемущества:
        1. Можно обращаться отдельно к ключам
        2. Можно будет менять поведение как будет нужно
"""
class Dictionary:
    __nodes = []
    __type = None

    ############################# ПУБЛИЧНЫЕ МЕТОДЫ #############################
    
    # добавление новой записи
    def add(self, key, value):
        if self.check_key(key):
            if self.check_value(value):
                self.__nodes.append(self.Node(key, value))
    
    # возвращает запись по индексу
    def get(self, index):
        return self.__nodes[index]
    
    # возвращает размер словаря
    def size(self):
        return len(self.__nodes)
    
    # возвращает лист из значений словаря
    def to_list(self):
        values = []
        nodes = self.__nodes
        for node in nodes:
            values.append(node.value)
        return values
    
    # проставляет обязательный тип данных
    def set_data_type(self, type):
        self.__type = type
    

    ############################# ПРИВАТНЫЕ МЕТОДЫ #############################

    # проверка на схожесть ключа
    def check_key(self, key):
        nodes = self.__nodes
        for node in nodes:
            if node.key == key:
                return False
        return True
    
    # проверка(-и) значения
    def check_value(self, value):
        if self.__type is not None: # у нас есть заданный тип данных
            if self.__type is not value: # value равен заданному типу данных
                return True
        return False
    
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
