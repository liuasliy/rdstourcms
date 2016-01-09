# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160110_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdsuser',
            name='headImage',
            field=models.ImageField(null=True, upload_to=b'media/upload', blank=True),
            preserve_default=True,
        ),
    ]
