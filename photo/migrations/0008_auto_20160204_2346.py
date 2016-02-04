# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_auto_20160204_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolist',
            name='pub_date',
            field=models.DateTimeField(default=b'2016-01-01', verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
    ]
