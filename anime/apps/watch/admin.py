from django.contrib import admin

from .models import Anime, ConstantGenre, Genre, AnimeComment


class AnimeAdmin(admin.ModelAdmin):
    model = Anime
    list_display = ['id', 'title_rus', 'title_foreign', 'season', 'episodes_quantity', 'start_date', 'tags']
    list_editable = ['title_rus', 'title_foreign', 'season', 'episodes_quantity', 'start_date', 'tags']
    list_filter = ['season', 'episodes_quantity']


class AnimeCommentAdmin(admin.ModelAdmin):
    model = AnimeComment
    list_display = ['id', 'author', 'anime', 'text']
    list_editable = ['author', 'anime', 'text']


class ConstantGenreAdmin(admin.ModelAdmin):
    model = ConstantGenre
    list_display = ['id', 'name', 'order_number']
    list_editable = ['name', 'order_number']


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_filter = ['anime']


admin.site.register(Anime, AnimeAdmin)
admin.site.register(AnimeComment, AnimeCommentAdmin)
admin.site.register(ConstantGenre, ConstantGenreAdmin)
admin.site.register(Genre, GenreAdmin)
