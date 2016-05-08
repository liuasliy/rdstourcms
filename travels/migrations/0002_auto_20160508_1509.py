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
            field=models.CharField(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', max_length=150, editable=False),
            preserve_default=True,
        ),
    ]
