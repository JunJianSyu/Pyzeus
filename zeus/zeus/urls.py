from django.conf.urls import patterns, include, url
from mobile.views import index

__author__ = 'JunJianSyu'

urlpatterns = patterns(
    '',
    url(r'^$', 'mobile.views.index', name='mobile'),
)

