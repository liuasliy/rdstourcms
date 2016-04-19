# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='author',
            field=models.CharField(max_length=150, editable=False),
            preserve_default=True,
        ),
    ]
