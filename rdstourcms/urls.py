from django.conf.urls import patterns, include, url
from django.contrib import admin
import  settings
from django.conf.urls.defaults import *


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'rdstourcms.views.home', name='home'),
                       url(r'^index/$', 'blog.views.index',name='index'),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^blog/(?P<blog_id>\d+)/$', 'blog.views.detail', name='detail'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.DIR_Admin}),
                       (r'^comments/', include('django_comments.urls')),
                       #url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_DIR}),
                       #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
                       url(r'^uploadimg/', 'blog.views.uploadimage'),

                       url(r'^media/(?P<path>(\S)*)', 'django.views.static.serve', {'document_root': 'media'}),
                       url(r'^login/$', 'blog.views.login', name='login'),
                       url(r'^register/$', 'blog.views.register'),
                       (r'^accounts/', include('userena.urls')),
                       url(r'^search/$', 'blog.views.search', name="search"),

                       url(r'^photo/', include('photo.urls')),
                       url(r'^photo/(?P<photos_id>\d+)/$', 'photo.views.photodetail', name='photodetail'),
                       #url(r'^photodetail/$', 'photo.views.photodetail', name='photodetail'),
                       url(r'^ajax_get_photo/$', 'photo.views.ajax_get_photo',name="ajax_get_photo"),


)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
