# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photolist_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolist',
            name='pub_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
