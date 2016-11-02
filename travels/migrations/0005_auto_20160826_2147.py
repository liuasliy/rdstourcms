# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_auto_20160826_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='setout_cost',
            field=models.IntegerField(verbose_name=b'\xe4\xba\xba\xe5\x9d\x87\xe8\xb4\xb9\xe7\x94\xa8'),
            preserve_default=True,
        ),
    ]
