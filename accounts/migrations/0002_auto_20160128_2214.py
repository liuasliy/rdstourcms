# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '\u6743\u9650\u7ba1\u7406',
                'verbose_name_plural': '\u6743\u9650\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoleList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('permission', models.ManyToManyField(to='accounts.PermissionList', null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u89d2\u8272\u7ba1\u7406',
                'verbose_name_plural': '\u89d2\u8272\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='myprofile',
            options={'verbose_name': '\u7528\u6237\u7ba1\u7406', 'verbose_name_plural': '\u7528\u6237\u7ba1\u7406'},
        ),
    ]
