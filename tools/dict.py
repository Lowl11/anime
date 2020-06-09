class Dictionary:
    """ Dictionary - кастомный словарь "ключ - значение". """

    __nodes = []
    __type = None

    ####################################################################
    ######################## ПУБЛИЧНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def __init__(self):
        self.clear()

    def add(self, key, value):
        """ добавление новой записи """

        if self.check_key(key):
            if self.check_value(value):
                self.__nodes.append(self.Node(key, value))

    def remove_by_key(self, key):
        """ удаление элемента по ключу """
        del self.__nodes[key]

    def remove_by_index(self, index):
        """ удаление по индексу """
        del self.__nodes[int(index)]

    def get_by_index(self, index):
        """ возвращает запись по индексу """
        return self.__nodes[index]

    def get_by_key(self, key):
        """ возвращает запись по ключу """

        nodes = self.__nodes
        for node in nodes:
            if node.key == key:
                return node.value
        return None

    def size(self):
        """ возвращает размер словаря """
        return len(self.__nodes)

    def to_list(self):
        """ возвращает лист из значений словаря """
        values = []
        nodes = self.__nodes
        for node in nodes:
            values.append(node.value)
        return values

    def to_assosiative(self):
        """ возвращает ассоциотивный массив """
        array = {}
        nodes = self.__nodes
        for node in nodes:
            array[node.key] = node.value
        return array

    def clear_from_empty(self):
        """ очистить от пустых значений """
        nodes = self.__nodes
        for node in nodes:
            if node.value is None or len(node.value) == 0:
                self.remove_by_key(node.key)
        return self

    def set_data_type(self, data_type):
        """ проставляет обязательный тип данных """
        self.__type = data_type

    def clear(self):
        """ очистика словаря """
        self.__nodes = []
        self.__type = None

    ####################################################################
    ######################## ПРИВАТНЫЕ МЕТОДЫ ##########################
    ####################################################################

    def check_key(self, key):
        """ проверка на схожесть ключа """

        nodes = self.__nodes
        for node in nodes:
            if node.key == key:
                return False
        return True

    def check_value(self, value):
        """ проверка(-и) значения """
        if self.__type is not None:  # у нас есть заданный тип данных
            if self.__type is not value:  # value равен заданному типу данных
                return True
        else:
            return True
        return False

    def __str__(self):
        """ перезапись метода toString() """

        result = ''
        nodes = self.__nodes
        for node in nodes:
            result += '{' + str(node.key) + ' : ' + str(node.value) + '}\n'
        return result

    class Node:
        """ Node - POKO класс служащий для хранения ключа и значения """

        key = None
        value = None

        def __init__(self, key, value):
            self.key = key
            self.value = value
