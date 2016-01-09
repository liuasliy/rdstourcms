# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20160110_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdsuser',
            name='headImage',
            field=models.ImageField(default=b'', upload_to=b'upload'),
            preserve_default=True,
        ),
    ]
