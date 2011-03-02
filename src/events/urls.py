from django.conf.urls.defaults import *

urlpatterns = patterns(
    'events.views',
    url(r'^$', 'object_list', {}, name='event_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', {}, name='event_detail'),
    )
