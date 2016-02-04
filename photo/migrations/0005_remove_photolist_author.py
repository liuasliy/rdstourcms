# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_remove_photolist_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photolist',
            name='author',
        ),
    ]
