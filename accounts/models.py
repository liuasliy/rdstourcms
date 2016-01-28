# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
# Create your models here.

# 定义权限
class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s(%s)' %(self.name, self.url)
    class Meta:
        verbose_name = '权限管理'
        verbose_name_plural = '权限管理'

# 定义角色
class RoleList(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList, null=True, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '角色管理'
        verbose_name_plural = '角色管理'

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    favourite_snack = models.CharField(_('favourite snack'), max_length=5)
    role = models.ForeignKey(RoleList, null=True, blank=True)
    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'




