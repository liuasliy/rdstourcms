#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
from photo.views import photopage
urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', photopage),


)
