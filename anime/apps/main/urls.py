from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.home_view, name = 'home_view'),
    url(r'^not-found/$', views.not_found_view, name = 'not_found_view'),
    ############################# /MAIN #######################################
]
