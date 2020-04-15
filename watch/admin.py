from django.contrib import admin

from .models import Anime, ConstantGenre, Genre

admin.site.register(Anime)
admin.site.register(ConstantGenre)
admin.site.register(Genre)