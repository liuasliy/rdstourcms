# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_myprofile_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='live_city',
            field=models.CharField(default=b'', max_length=80),
            preserve_default=True,
        ),
    ]
