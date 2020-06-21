from django.contrib import admin

# подключение кастомных классов
from .models import NavigationLink


class NavigationLinkAdmin(admin.ModelAdmin):
    """ админ класс моделей """
    model = NavigationLink
    list_display = ['id', 'name', 'url', 'order_number']
    list_editable = ['name', 'url', 'order_number']


# регистрация моделей БД в админ-панели
admin.site.register(NavigationLink, NavigationLinkAdmin)


# кастомизация админки
admin.site.site_header = 'ANIME - Админ панель'
