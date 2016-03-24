# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritetravels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(default=b'', upload_to=b'upload')),
                ('pub_date', models.DateTimeField()),
                ('count_hit', models.IntegerField(default=0, editable=False)),
                ('tags', models.CharField(max_length=100)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6e38\u8bb0\u7ba1\u7406',
                'verbose_name_plural': '\u6e38\u8bb0\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='favoritetravels',
            name='travels',
            field=models.ForeignKey(to='travels.Travels'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favoritetravels',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
