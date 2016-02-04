# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20160204_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolist',
            name='user',
            field=models.OneToOneField(default=b'', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
