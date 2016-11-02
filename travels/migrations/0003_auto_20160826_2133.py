# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0002_auto_20160826_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='setout_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe5\x87\xba\xe5\x8f\x91\xe6\x97\xb6\xe9\x97\xb4', blank=True),
            preserve_default=True,
        ),
    ]
