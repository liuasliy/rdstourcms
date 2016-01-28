# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_favoriteblog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': '\u6e38\u8bb0\u7ba1\u7406', 'verbose_name_plural': '\u6e38\u8bb0\u7ba1\u7406'},
        ),
    ]
