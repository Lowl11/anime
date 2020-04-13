from django.shortcuts import render, redirect

class Starter:
    # Определение с какого модуля начинается приложение
    @staticmethod
    def start_from():
        return 'watch'
    
    # Редайрект на Not Found, Action метод
    @staticmethod
    def not_found_method():
        return redirect('/not-found/')
