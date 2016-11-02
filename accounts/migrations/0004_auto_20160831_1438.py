# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_myprofile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='nickname',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myprofile',
            name='personal_brief',
            field=models.TextField(default=b'', verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b'),
            preserve_default=True,
        ),
    ]
