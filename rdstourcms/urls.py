from django.conf.urls import patterns, include, url
from django.contrib import admin
import  settings
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include




urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'rdstourcms.views.index', name='home'),
                       url(r'^index/$', 'rdstourcms.views.index', name='index'),
                       url(r'^travels/', include('travels.urls')),
                       url(r'^travels/(?P<travels_id>\d+)/$', 'travels.views.detail', name='detail'),
                       url(r'^city/(?P<city>\w+)/$', 'travels.views.search_city', name='search_city'),

                       #url(r'^favlist/$', 'favourite.views.favlist', name='favlist'),


                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.DIR_Admin}),
                       (r'^comments/', include('django_comments.urls')),
                       #url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_DIR}),
                       #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
                       url(r'^uploadimg/', 'travels.views.uploadimage'),

                       url(r'^media/(?P<path>(\S)*)', 'django.views.static.serve', {'document_root': 'media'}),
                       url(r'^login/$', 'travels.views.login', name='login'),
                       url(r'^register/$', 'travels.views.register'),
                       url(r'^logout/$', 'travels.views.logout',),
                       (r'^accounts/', include('userena.urls')),
                       url(r'^search/$', 'travels.views.search', name="search"),

                       url(r'^photo/', include('photo.urls')),
                       url(r'^photo/(?P<photos_id>\d+)/$', 'photo.views.photodetail', name='photodetail'),
                       #url(r'^photodetail/$', 'photo.views.photodetail', name='photodetail'),
                       url(r'^ajax_get_photo/$', 'photo.views.ajax_get_photo',name="ajax_get_photo"),

                       url(r'^add/$', 'travels.views.add',name="add"),
                       url(r'^updatetra/(?P<travels_id>\d+)/$', 'travels.views.updatetra',name="updatetra"),
                       url(r'^deletetra/(?P<travels_id>\d+)/$', 'travels.views.deletetra',name="deletetra"),
                       url(r'^list/(?P<author>\w+)/$', 'travels.views.list',name="list"),

                       url(r'^addfav/(?P<travels_id>\d+)/$', 'favourite.views.add_favorite',name="add_favorite"),
                       url(r'^favlist/(?P<user>\w+)/$', 'favourite.views.favourite_list',name="favourite_list"),
                       url(r'^deletefav/(?P<favourite_id>\d+)/$', 'favourite.views.deletefav',name="deletefav"),


                       url(r'^like_photo/(?P<photos_id>\d+)/$', 'photo.views.like_photo',name="like_photo"),




)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
