# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.OneToOneField(to='travels.Travels')),
            ],
            options={
                'verbose_name': '\u6536\u85cf\u5939\u5217\u8868',
                'verbose_name_plural': '\u6536\u85cf\u5939\u5217\u8868',
            },
            bases=(models.Model,),
        ),
    ]
