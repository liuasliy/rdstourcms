# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photolist',
            name='photointro',
            field=ckeditor.fields.RichTextField(default=b'', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xbb\x8b\xe7\xbb\x8d'),
            preserve_default=True,
        ),
    ]
