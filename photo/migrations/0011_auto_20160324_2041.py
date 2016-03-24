# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_auto_20160324_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolist',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'upload/photo/'),
            preserve_default=True,
        ),
    ]
