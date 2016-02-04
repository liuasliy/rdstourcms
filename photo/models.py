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
    photo = models.ImageField(upload_to='upload', default='')
    user = models.OneToOneField(User, default='')
    pubdate = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '摄影照片'
        verbose_name_plural = '摄影照片'

class photoListAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user.username

        obj.save()

admin.site.register(photoList, photoListAdmin)

