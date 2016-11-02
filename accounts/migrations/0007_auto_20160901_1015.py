# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myprofile_live_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='favourite_snack',
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='live_city',
            field=models.CharField(default=b'', max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='personal_brief',
            field=models.TextField(default=b'', null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b', blank=True),
            preserve_default=True,
        ),
    ]
