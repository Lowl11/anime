from django.shortcuts import render, redirect

class Starter:
    # определение с какого модуля начинается приложение (клиентская сторона - main)
    @staticmethod
    def main_start_from():
        return 'watch'
    
    # определяем с чего начинается CMS
    @staticmethod
    def cms_start_from():
        return 'anime'
    
    # URL сервера с ElasticSearch
    @staticmethod
    def es_nodes():
        return ['http://127.0.0.1:9200']
    
    # редайрект на Not Found, Action метод
    @staticmethod
    def not_found_method():
        return redirect('/not-found/')
