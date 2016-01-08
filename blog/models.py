# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = RichTextField()
    image = models.ImageField(upload_to='upload', default='')
    timestamp = models.DateTimeField()
    tags = models.CharField(max_length=100)
    author = models.CharField(max_length=50)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
