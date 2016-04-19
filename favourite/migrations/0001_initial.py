# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': '\u6536\u85cf\u5939\u5217\u8868',
                'verbose_name_plural': '\u6536\u85cf\u5939\u5217\u8868',
            },
            bases=(models.Model,),
        ),
    ]
