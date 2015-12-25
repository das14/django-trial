# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libmanaiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_link',
            field=models.CharField(default=b'http://www.clker.com/cliparts/6/4/J/9/E/9/closed-book-md.png', max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='number_of_copies',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
