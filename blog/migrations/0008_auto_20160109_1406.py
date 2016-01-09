# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20160107_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='RdsUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('per_img', models.ImageField(null=True, upload_to=b'upload', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('autograph', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='timestamp',
            new_name='pub_date',
        ),
    ]
