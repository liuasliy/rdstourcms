# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0013_auto_20160508_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='photolist',
            name='tag',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe7\x85\xa7\xe7\x89\x87\xe6\xa0\x87\xe7\xad\xbe'),
            preserve_default=True,
        ),
    ]
