# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20160204_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photolist',
            name='pub_date',
        ),
    ]
