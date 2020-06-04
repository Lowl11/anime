from django.contrib import admin

# подключение кастомных классов
from .models import CmsNavigationLink, File, Folder, CmsMainInfo

# админ класс моделей
class CmsNavigationLinkAdmin(admin.ModelAdmin):
    model = CmsNavigationLink
    list_display = ['id', 'name', 'url', 'order_number', 'glyph_icon']
    list_editable = ['name', 'url', 'order_number', 'glyph_icon']

class CmsMainInfoAdmin(admin.ModelAdmin):
    model = CmsMainInfo
    list_display = ['id', 'main_notification', 'mini_notification1', 'mini_notification2']
    list_editable = ['main_notification', 'mini_notification1', 'mini_notification2']

# регистрация моделей БД в админ-панели
admin.site.register(CmsNavigationLink, CmsNavigationLinkAdmin)
admin.site.register(File)
admin.site.register(Folder)
admin.site.register(CmsMainInfo)
