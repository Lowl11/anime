from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.home_view, name='cms_home_view'),
    url(r'^anime/$', views.anime_view, name='cms_anime_view'),
    url(r'^dashboard/$', views.dashboard_view, name='cms_dashboard_view'),
    url(r'^elastic/$', views.elastic_view, name = 'cms_elastic_view'),
    url(r'^fm/$', views.fm_view, name = 'cms_fm_view'),

    ### Manage Anime ###
    url(r'^anime/new/$', views.anime_new_view, name = 'cms_new_anime_view'),
    url(r'^anime/manage/(?P<pk>\d+)', views.manage_anime_view, name='cms_manage_anime_view'),
    url(r'^anime/manage/$', views.manage_anime_post, name = 'cms_manage_anime_post'),

    #### ElasticSearch ###
    url(r'^elastic/delete-index/(?P<index_name>.*)/$', views.elastic_delete_index_ajax, name = 'cms_elastic_delete_index_ajax'),
    url(r'^elastic/fill/(?P<data_type>\w+)/$', views.elastic_fill_get, name = 'cms_elastic_fill_get'),

    ### FileManager ###
    url(r'^fm/objects/$', views.fm_objects_get, name = 'cms_fm_objects_get'),
    url(r'^fm/create_folder/$', views.fm_create_folder_get, name = 'cms_fm_create_folder_get'),
    url(r'^fm/rename_folder/$', views.fm_rename_folder_get, name = 'cms_fm_rename_folder_get'),
    url(r'^fm/delete_folder/$', views.fm_delete_folder_get, name = 'cms_fm_delete_folder_get'),
    ############################# /MAIN #######################################
]
