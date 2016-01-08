# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=b'', upload_to=b'upload'),
            preserve_default=True,
        ),
    ]
