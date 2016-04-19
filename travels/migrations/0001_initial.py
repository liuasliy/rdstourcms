# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField()),
                ('contextinfo', models.TextField(default=b'', verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('image', models.ImageField(default=b'', upload_to=b'upload/travels/', verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\xa4\xa7\xe5\x9b\xbe')),
                ('bigimage', models.ImageField(default=b'', upload_to=b'upload/travels/', verbose_name=b'\xe9\xa1\xb6\xe9\x83\xa8\xe5\xa4\xa7\xe8\x83\x8c\xe6\x99\xaf')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('count_hit', models.IntegerField(default=0, editable=False)),
                ('city', models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82')),
                ('author', models.CharField(max_length=150)),
                ('author_id', models.IntegerField(editable=False)),
            ],
            options={
                'verbose_name': '\u6e38\u8bb0\u7ba1\u7406',
                'verbose_name_plural': '\u6e38\u8bb0\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
    ]
