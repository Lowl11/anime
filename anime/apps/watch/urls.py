from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.page_view, name='watch_page_view'),
    url(r'^anime/(?P<pk>\d+)$', views.anime_view, name = 'watch_anime_view'),
    url(r'^genre/(?P<name>.*)$', views.genre_view, name = 'watch_genre_view'),
    url(r'^year/(?P<year>\d+)$', views.year_view, name = 'watch_year_view'),
    url(r'^xsearch/$', views.xsearch_get, name = 'xsearch_get'),
    url(r'^comment/$', views.comment_post, name = 'watch_comment_post'),
    ############################# /MAIN #######################################
]
