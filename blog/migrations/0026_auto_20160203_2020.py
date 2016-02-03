# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20160128_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdsuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='RdsUser',
        ),
    ]
