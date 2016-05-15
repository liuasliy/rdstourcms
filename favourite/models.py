# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from travels.models import Travels
from django.contrib.auth.models import User

# Create your models here.
class Favourite(models.Model):
    user = models.ForeignKey(User, default="")
    travels = models.ForeignKey(Travels, default="")

    def __unicode__(self):
        return self.travels.title

    class Meta:
        verbose_name = '游记标题'
        verbose_name_plural = '收藏夹列表'


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('travels', 'user')

admin.site.register(Favourite, FavouriteAdmin)

