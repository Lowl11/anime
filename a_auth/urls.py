from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# AUTH #################################
    url(r'^signup/$', views.signup_view, name='signup_view'),
    # url(r'^register_post/$', views.register_post, name='register_post'),

    url(r'^signin/$', views.signin_view, name='signin_view'),
    # url(r'^login_post/$', views.login_post, name='login_post'),
    url(r'^logout/$', views.logout_get, name='logout_get'),
    ############################# /AUTH ################################
]
