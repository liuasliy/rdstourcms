# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

# Create your models here.

class photoList(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='upload/photo/', default='')
    photointro = RichTextField('图片介绍', default='')
    user = models.ForeignKey(User, default="")
    pubdate = models.DateTimeField('发布日期', default=timezone.now)
    count_hit = models.IntegerField(default=0, editable=False)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '摄影照片'
        verbose_name_plural = '摄影照片'



admin.site.register(photoList)

