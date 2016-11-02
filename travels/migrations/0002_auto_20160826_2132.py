# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='setout_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x87\xba\xe5\x8f\x91\xe6\x97\xb6\xe9\x97\xb4', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='travels',
            name='setout_days',
            field=models.IntegerField(default=b'', verbose_name=b'\xe5\x87\xba\xe8\xa1\x8c\xe5\xa4\xa9\xe6\x95\xb0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='travels',
            name='setout_people',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe4\xba\xba\xe7\x89\xa9'),
            preserve_default=True,
        ),
    ]
