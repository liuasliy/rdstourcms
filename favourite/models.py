# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from travels.models import Travels

# Create your models here.
class Favourite(models.Model):
    title = models.CharField(max_length=150)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '收藏夹列表'
        verbose_name_plural = '收藏夹列表'


admin.site.register(Favourite)

