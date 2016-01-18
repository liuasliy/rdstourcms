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
    count_hit = models.IntegerField(default=0,editable=False)
    tags = models.CharField(max_length=100)
    author = models.OneToOneField(User)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(BlogPost, BlogPostAdmin)



# 给注册用户添加头像
class RdsUser(models.Model):
    description = models.TextField(max_length=256, default="", blank=True)
    headImage = models.ImageField(upload_to='upload', default='')
    user = models.OneToOneField(User)


# 收藏
class FavoriteBlog(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey(BlogPost)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s likes blog %s" % (self.user, self.blog)



