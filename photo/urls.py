from django.conf.urls.defaults import *
from photo.views import photopage
urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', photopage),


)
