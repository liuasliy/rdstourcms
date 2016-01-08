# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_item_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=b'upload/20160102220000_avatar-1.jpg', upload_to=b'upload'),
            preserve_default=True,
        ),
    ]
