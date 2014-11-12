from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    url(r'^$', 'explore.views.home', name='home'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/$', 'explore.views.explore'),
    url(r'^explore/static/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/(?P<plot_type>[a-z_]+)/(?P<target_id>[A-za-z0-9]+)/$', 'explore.views.static'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/(?P<data_type>[a-z_]+)/(?P<target_id>[A-za-z0-9]+)/$', 'explore.views.get_data'),
    url(r'^about/$', redirect_to, {'url': '/about/self/'}),
    url(r'^about/(?P<about_type>[a-z_]+)/$', 'explore.views.about'),
    url(r'^question/$', 'explore.views.question'),

    url(r'^debug/$', 'explore_debug.views.home', name='home'),
    url(r'^debug/explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/$', 'explore_debug.views.explore'),
    url(r'^debug/explore/static/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/(?P<plot_type>[a-z_]+)/(?P<target_id>[A-za-z0-9]+)/$', 'explore_debug.views.static'),
    url(r'^debug/explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/(?P<data_type>[a-z_]+)/(?P<target_id>[A-za-z0-9]+)/$', 'explore_debug.views.get_data'),
    url(r'^debug/about/$', redirect_to, {'url': '/debug/about/self/'}),
    url(r'^debug/about/(?P<about_type>[a-z_]+)/$', 'explore_debug.views.about'),
    url(r'^debug/question/$', 'explore_debug.views.question'),

)
