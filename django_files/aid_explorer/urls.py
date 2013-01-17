from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'explore.views.home', name='home'),
    url(r'^explore/(?P<app_type>[a-z_]+)/(?P<entity_id>\d+)/$', 'explore.views.explore'),
)
