from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.page_view, name='watch_page_view'),
    ############################# /MAIN #######################################
]
