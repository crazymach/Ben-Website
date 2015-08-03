
from django.conf.urls import patterns, url

from input import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^s/$', views.subproject, name='subproject')
)