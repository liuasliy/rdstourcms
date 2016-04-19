# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Travels(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    contextinfo = models.TextField('简介', default='')
    image = models.ImageField('首页大图', upload_to='upload/travels/', default='')
    bigimage = models.ImageField('顶部大背景', upload_to='upload/travels/', default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    count_hit = models.IntegerField(default=0, editable=False)
    city = models.CharField('城市', max_length=100, default='')
    author = models.CharField(max_length=150, editable=False)
    author_id = models.IntegerField(editable=False)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '游记管理'
        verbose_name_plural = '游记管理'


class TravelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    def save_model(self, request, obj, form, change):
        obj.author = request.user.username
        obj.author_id = request.user.id
        obj.save()

admin.site.register(Travels, TravelsAdmin)






