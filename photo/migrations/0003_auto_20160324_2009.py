# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photolist_photointro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolist',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'upload/photo'),
            preserve_default=True,
        ),
    ]
