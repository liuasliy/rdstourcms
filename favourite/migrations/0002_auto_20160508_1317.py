# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favourite',
            options={'verbose_name': '\u6e38\u8bb0\u6807\u9898', 'verbose_name_plural': '\u6536\u85cf\u5939\u5217\u8868'},
        ),
        migrations.AddField(
            model_name='favourite',
            name='isfav',
            field=models.BooleanField(default=b''),
            preserve_default=True,
        ),
    ]
