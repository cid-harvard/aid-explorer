from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'explore.views.home', name='home'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/$', 'explore.views.explore'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/(?P<data_type>[a-z_]+)/(?P<target_id>[A-za-z0-9]+)/$', 'explore.views.get_data'),
    url(r'^about/(?P<about_type>[a-z_]+)/$', 'explore.views.about'),
)
