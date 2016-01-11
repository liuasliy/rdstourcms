# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    image = models.ImageField(upload_to='upload', default='')
    pub_date = models.DateTimeField()
    count_hit = models.IntegerField(default=0, editable=False, verbose_name=u'点击数')
    tags = models.CharField(max_length=100)
    author = models.CharField(max_length=50)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(BlogPost, BlogPostAdmin)

# 计数器
class Count(models.Model):
    num = models.IntegerField(default=0, verbose_name=u'+1数')
    blog = models.ForeignKey(BlogPost)
    def __unicode__(self):
        return self.num


# 给注册用户添加头像
class RdsUser(models.Model):
    description = models.TextField(max_length=256, default="", blank=True)
    headImage = models.ImageField(upload_to='upload', default='')
    user = models.OneToOneField(User)




