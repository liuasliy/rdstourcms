# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_auto_20160330_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='contextinfo',
            field=models.TextField(default=b'', verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
            preserve_default=True,
        ),
    ]
