from django.contrib import admin

# подключение кастомных классов
from .models import NavigationLink

# админ класс моделей
class NavigationLinkAdmin(admin.ModelAdmin):
    model = NavigationLink
    list_display = ['id', 'name', 'url']
    list_editable = ['name', 'url']

# регистрация моделей БД в админ-панели
admin.site.register(NavigationLink, NavigationLinkAdmin)


# кастомизация админки
admin.site.site_header = 'ANIME - Админ панель'
