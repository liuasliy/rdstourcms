# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('travels', models.ForeignKey(default=b'', to='travels.Travels')),
                ('user', models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6536\u85cf\u5939\u5217\u8868',
                'verbose_name_plural': '\u6536\u85cf\u5939\u5217\u8868',
            },
            bases=(models.Model,),
        ),
    ]
