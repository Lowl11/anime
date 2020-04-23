from django.contrib import admin

# подключение кастомных классов
from .models import CmsNavigationLink

# админ класс моделей
class CmsNavigationLinkAdmin(admin.ModelAdmin):
    model = CmsNavigationLink
    list_display = ['id', 'name', 'url', 'order_number', 'glyph_icon']
    list_editable = ['name', 'url', 'order_number', 'glyph_icon']

# регистрация моделей БД в админ-панели
admin.site.register(CmsNavigationLink, CmsNavigationLinkAdmin)
