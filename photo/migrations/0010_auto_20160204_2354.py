# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0009_auto_20160204_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photolist',
            old_name='pub_date',
            new_name='pubdate',
        ),
    ]
