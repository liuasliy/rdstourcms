# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0002_auto_20160508_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='isfav',
        ),
    ]
