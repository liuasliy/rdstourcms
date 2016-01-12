# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160111_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='count',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Count',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='count_hit',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
