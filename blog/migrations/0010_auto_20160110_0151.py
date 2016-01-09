# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0001_initial'),
        ('blog', '0009_auto_20160110_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='RdsUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', max_length=256, blank=True)),
                ('headImage', models.ImageField(null=True, upload_to=b'upload/users/', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
