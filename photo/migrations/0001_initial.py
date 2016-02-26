# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='photoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('photo', models.ImageField(default=b'', upload_to=b'upload')),
                ('pubdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
                ('user', models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6444\u5f71\u7167\u7247',
                'verbose_name_plural': '\u6444\u5f71\u7167\u7247',
            },
            bases=(models.Model,),
        ),
    ]
