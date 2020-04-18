class Utils:
    @staticmethod
    def try_get_from_request(request, type, name):
        try:
            if type == 'POST':
                return request.POST[name]
            elif type == 'GET':
                return request.GET[name]
            elif type == 'SESSION':
                print('')
                print('Utils')
                print('try_get_from_request')
                print('name: ' + name)
                print(request.session[name])
                print('')
                return request.session[name]
            else:
                raise Exception('Данный тип запроса не поддерживается')
        except:
            return ''
