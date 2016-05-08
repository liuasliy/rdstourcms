# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0012_photolist_count_hit'),
    ]

    operations = [
        migrations.AddField(
            model_name='photolist',
            name='praise_num',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photolist',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'upload/photo/', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photolist',
            name='photointro',
            field=ckeditor.fields.RichTextField(default=b'', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87\xe4\xbb\x8b\xe7\xbb\x8d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photolist',
            name='title',
            field=models.CharField(max_length=150, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=True,
        ),
    ]
