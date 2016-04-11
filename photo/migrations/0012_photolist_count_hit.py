# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0011_auto_20160324_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='photolist',
            name='count_hit',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
    ]
