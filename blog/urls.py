from django.conf.urls.defaults import *
from blog.views import archive
urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', archive),

)
