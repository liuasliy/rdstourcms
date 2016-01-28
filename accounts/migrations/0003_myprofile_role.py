# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160128_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='role',
            field=models.ForeignKey(blank=True, to='accounts.RoleList', null=True),
            preserve_default=True,
        ),
    ]
