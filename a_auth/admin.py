from django.contrib import admin

from .models import Viewer, Role

class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display = ['id', 'name', 'value']
    list_editable = ['name', 'value']

admin.site.register(Viewer)
admin.site.register(Role, RoleAdmin)