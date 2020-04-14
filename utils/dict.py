class Dictionary:
    __nodes = []

    def add(self, key, value):
        if self.check_key(key):
            self.__nodes.append(self.Node(key, value))
        
    def get(self, index):
        return self.__nodes[index]
    
    def size(self):
        return len(self.__nodes)
    
    def check_key(self, key):
        nodes = self.__nodes
        for node in nodes:
            if node.key == key:
                return False
        return True
    
    def __str__(self):
        result = ''
        nodes = self.__nodes
        for node in nodes:
            result += '{' + str(node.key) + ' : ' + str(node.value) + '}\n'
        return result
        
    class Node:
        key = None
        value = None

        def __init__(self, key, value):
            self.key = key
            self.value = value
