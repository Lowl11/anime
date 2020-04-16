from django.contrib import admin

from .models import Anime, ConstantGenre, Genre

class AnimeAdmin(admin.ModelAdmin):
    model = Anime
    list_display = ['id', 'title_rus', 'title_foreign', 'season', 'episodes_quantity']
    list_editable = ['title_rus', 'title_foreign', 'season', 'episodes_quantity', ]


class ConstantGenreAdmin(admin.ModelAdmin):
    model = ConstantGenre
    list_display = ['id', 'name', 'order_number']
    list_editable = ['name', 'order_number']

admin.site.register(Anime, AnimeAdmin)
admin.site.register(ConstantGenre, ConstantGenreAdmin)
admin.site.register(Genre)
