# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160831_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='sex',
            field=models.CharField(default=b'', max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')]),
            preserve_default=True,
        ),
    ]
