# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from travels.models import Travels

# Create your models here.
class Favourite(models.Model):
    title = models.CharField(max_length=150)
    contextinfo = models.TextField('简介', default='')
    image = models.ImageField('首页大图', upload_to='upload/travels/', default='')
    count_hit = models.IntegerField(default=0, editable=False)
    author = models.CharField(max_length=150, editable=False)
    author_id = models.IntegerField(editable=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '收藏夹列表'
        verbose_name_plural = '收藏夹列表'


admin.site.register(Favourite)

