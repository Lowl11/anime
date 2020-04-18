from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.page_view, name='watch_page_view'),
    url(r'^anime/(?P<pk>\d+)$', views.anime_view, name='watch_anime_view'),
    url(r'^genre/(?P<name>.*)$', views.genre_view, name='watch_genre_view'),
    ############################# /MAIN #######################################
]
