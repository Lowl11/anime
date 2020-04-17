class Utils:
    @staticmethod
    def try_get_from_request(request, type, name):
        try:
            if type == 'POST':
                return request.POST[name]
            elif type == 'GET':
                return request.GET[name]
            else:
                raise Exception('Данный тип запроса не поддерживается')
        except E:
            return ''
