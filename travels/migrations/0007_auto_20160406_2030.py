# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0006_auto_20160406_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travels',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='travels',
            name='city',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82'),
            preserve_default=True,
        ),
    ]
