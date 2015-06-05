from django.conf.urls import patterns, include, url

__author__ = 'JunJianSyu'

from mobile.views import index

urlpatterns = patterns(
    '',
    url(r'^$', 'mobile.views.index', name='mobile'),
)

