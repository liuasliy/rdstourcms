# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20160117_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='count_hit',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
    ]
