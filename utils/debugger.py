class Debugger:
    # более удобный вывод в терминал
    @staticmethod
    def write(msg, description = None):
        print('')
        if description is not None:
            print(description)
        print(msg)
        print('')
    
