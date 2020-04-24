from django.shortcuts import render, redirect

# определение с какого модуля начинается приложение (клиентская сторона - main)
def main_start_from():
    return 'watch'

# определяем с чего начинается CMS
def cms_start_from():
    return 'anime'

# URL сервера с ElasticSearch
def es_node():
    return 'http://127.0.0.1:9200'

# редайрект на Not Found, Action метод
def not_found_method():
    return redirect('/not-found/')
