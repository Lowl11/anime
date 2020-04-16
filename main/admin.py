from django.contrib import admin

from .models import NavigationLink

class NavigationLinkAdmin(admin.ModelAdmin):
    model = NavigationLink
    list_display = ['id', 'name', 'url']
    list_editable = ['name', 'url']

# Регистрация моделей БД в админ-панели
admin.site.register(NavigationLink, NavigationLinkAdmin)