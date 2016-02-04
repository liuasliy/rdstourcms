# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_auto_20160204_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolist',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
