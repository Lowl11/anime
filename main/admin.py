from django.contrib import admin

from .models import NavigationLink

# Регистрация моделей БД в админ-панели
admin.site.register(NavigationLink)