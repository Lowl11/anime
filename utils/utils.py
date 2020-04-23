class Utils:
    # пытатется вернуть значение с массива по названию с реквеста
    @staticmethod
    def try_get_from_request(request, type, name):
        try:
            if type == 'POST':
                return request.POST[name]
            elif type == 'GET':
                return request.GET[name]
            elif type == 'SESSION':
                return request.session[name]
            else:
                raise Exception('Данный тип запроса не поддерживается')
        except:
            return ''
    
    # пытается вернуть значение с массива по названию
    @staticmethod
    def try_get_from_array(array, name):
        try:
            return array[name]
        except:
            return None
        
    # вырезает пустые строки в массиве
    @staticmethod
    def erase_empty_strings(array):
        result = []
        for word in array:
            if len(word) > 0:
                result.append(word)
        return result
