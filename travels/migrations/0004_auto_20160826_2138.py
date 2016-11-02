# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_auto_20160826_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='setout_days',
            field=models.IntegerField(verbose_name=b'\xe5\x87\xba\xe8\xa1\x8c\xe5\xa4\xa9\xe6\x95\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='travels',
            name='setout_people',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xba\xba\xe7\x89\xa9'),
            preserve_default=True,
        ),
    ]
