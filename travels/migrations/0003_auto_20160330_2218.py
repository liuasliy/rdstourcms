# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0002_auto_20160324_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='bigimage',
            field=models.ImageField(default=b'', upload_to=b'upload/travels/', verbose_name=b'\xe9\xa1\xb6\xe9\x83\xa8\xe5\xa4\xa7\xe8\x83\x8c\xe6\x99\xaf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='travels',
            name='image',
            field=models.ImageField(default=b'', upload_to=b'upload/travels/', verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\xa4\xa7\xe5\x9b\xbe'),
            preserve_default=True,
        ),
    ]
