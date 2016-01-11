# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20160110_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(default=0, verbose_name='+1\u6570')),
                ('blog', models.ForeignKey(to='blog.BlogPost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='count_hit',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570', editable=False),
            preserve_default=True,
        ),
    ]
