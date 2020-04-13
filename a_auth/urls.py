from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# AUTH #################################
    # url(r'^register/$', views.register_view, name='register_view'),
    # url(r'^register_post/$', views.register_post, name='register_post'),

    # url(r'^login/$', views.login_view, name='login_view'),
    # url(r'^login_post/$', views.login_post, name='login_post'),
    # url(r'^logout/$', views.logout_get, name='logout_get'),
    ############################# /AUTH ################################
]
