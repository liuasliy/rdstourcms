# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.


class Travels(models.Model):
    title = models.CharField('标题', max_length=150)
    setout_date = models.DateTimeField('出发时间', null=True, blank=True)
    setout_days = models.IntegerField('出行天数')
    setout_people = models.CharField('人物', max_length=100)
    setout_cost = models.IntegerField('人均费用')
    content = RichTextField('正文')
    contextinfo = models.TextField('简介', default='')
    image = models.ImageField('首页大图', upload_to='upload/travels/%Y/%m', default='')
    bigimage = models.ImageField('顶部大背景', upload_to='upload/travels/%Y/%m', default='')
    pub_date = models.DateTimeField('创建时间', auto_now_add=True)
    count_hit = models.IntegerField(default=0, editable=False)
    praise_num = models.IntegerField(default=0, editable=False)
    city = models.CharField('城市', max_length=100, default='')
    author = models.CharField('作者', max_length=150, editable=False)
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






