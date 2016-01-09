# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('blog', '0008_auto_20160109_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(default=b'', max_length=256, blank=True)),
                ('headImage', models.ImageField(null=True, upload_to=b'/media/upload/users/', blank=True)),
                ('scope', models.IntegerField(default=100)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.RemoveField(
            model_name='rdsuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='RdsUser',
        ),
    ]
