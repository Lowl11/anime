from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# AUTH #################################
    url(r'^signup/$', views.signup_view, name='signup_view'),
    url(r'^signup_post/$', views.signup_post, name='signup_post'),

    url(r'^signin/$', views.signin_view, name='signin_view'),
    url(r'^signin_post/$', views.signin_post, name='signin_post'),
    url(r'^logout/$', views.logout_get, name='logout_get'),
    ############################# /AUTH ################################
]
