from django.db import models
from django.contrib import admin
from blog.models import BlogPost

# Create your models here.
class Favourite(models.Model):
    title = models.OneToOneField(BlogPost)
    def __unicode__(self):
        return self.title


admin.site.register(Favourite)

