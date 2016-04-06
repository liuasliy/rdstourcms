# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_travels_contextinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travels',
            name='tags',
        ),
    ]
