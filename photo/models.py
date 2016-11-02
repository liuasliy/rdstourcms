# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

# Create your models here.

class photoList(models.Model):
    title = models.CharField('标题', max_length=150)
    photo = models.ImageField('照片',upload_to='upload/photo/%Y/%m', default='')
    photointro = RichTextField('照片介绍', default='')
    user = models.ForeignKey(User, default="")
    pubdate = models.DateTimeField('发布日期', default=timezone.now)
    count_hit = models.IntegerField(default=0, editable=False)
    praise_num = models.IntegerField(default=0, editable=False)
    tag = models.CharField('照片标签', max_length=100,default="")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '摄影照片'
        verbose_name_plural = '摄影照片'


class photoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'user')

admin.site.register(photoList, photoListAdmin)

