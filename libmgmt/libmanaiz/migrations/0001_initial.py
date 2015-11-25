# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_title', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField()),
                ('author', models.CharField(max_length=250)),
                ('publisher', models.CharField(max_length=250)),
                ('isbn', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('no_of_pages', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrowed_date', models.DateTimeField()),
                ('borrowed_reason', models.CharField(default=b'No reason provided', max_length=1000)),
                ('book', models.ForeignKey(to='libmanaiz.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='borrow',
            name='borrowed_by',
            field=models.ForeignKey(to='libmanaiz.Patron'),
        ),
    ]
