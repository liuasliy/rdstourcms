# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Travels(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    image = models.ImageField(upload_to='upload/travels/', default='')
    pub_date = models.DateTimeField()
    count_hit = models.IntegerField(default=0,editable=False)
    tags = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    class Meta:
        verbose_name = '游记管理'
        verbose_name_plural = '游记管理'


class TravelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Travels, TravelsAdmin)




# 收藏
class Favoritetravels(models.Model):
    user = models.ForeignKey(User)
    travels = models.ForeignKey(Travels)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s likes travels %s" % (self.user, self.travels)




