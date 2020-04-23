from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.home_view, name='cms_home_view'),
    url(r'^anime/$', views.anime_view, name='cms_anime_view'),
    url(r'^anime/manage/(?P<pk>\d+)', views.anime_manage_view, name='cms_anime_anime_manage_view'),
    url(r'^dashboard/$', views.dashboard_view, name='cms_dashboard_view'),
    url(r'^elastic/$', views.elastic_view, name = 'cms_elastic_view'),

    #### ElasticSearch ###
    url(r'^elastic/delete-index/(?P<index_name>.*)/$', views.elastic_delete_index_get, name = 'cms_elastic_delete_index_get'),
    url(r'^elastic/fill/(?P<data_type>\w+)/$', views.elastic_fill_get, name = 'cms_elastic_fill_get')
    ############################# /MAIN #######################################
]
