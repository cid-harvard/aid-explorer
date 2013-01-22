from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'explore.views.home', name='home'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/$', 'explore.views.explore'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/(?P<data_type>[a-z_]+)/(?P<target_id>\d+)/$', 'explore.views.get_data'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/(?P<data_type>[a-z_]+)/(?P<list_type>[A-Za-z_]+)/$', 'explore.views.get_list'),
)
