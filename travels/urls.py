#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
from travels.views import archive
urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', archive),

)
