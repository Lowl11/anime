from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.home_view, name='cms_home_view'),
    url(r'^anime/$', views.anime_view, name='cms_anime_view'),
    ############################# /MAIN #######################################
]
