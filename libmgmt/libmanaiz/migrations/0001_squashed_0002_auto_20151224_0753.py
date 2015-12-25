# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    replaces = [(b'libmanaiz', '0001_initial'), (b'libmanaiz', '0002_auto_20151224_0753')]

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
                ('isbn', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=50)),
                ('no_of_pages', models.PositiveIntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrowed_date', models.DateTimeField()),
                ('borrowed_reason', models.CharField(default=b'No reason provided', max_length=1000)),
                ('book_borrowed', models.ForeignKey(to='libmanaiz.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_value', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('date_of_rating', models.DateTimeField(auto_now_add=True)),
                ('rating_book', models.ForeignKey(to='libmanaiz.Book')),
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
            model_name='comment',
            name='rating_by',
            field=models.ForeignKey(to='libmanaiz.Patron'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='borrowed_by',
            field=models.ForeignKey(to='libmanaiz.Patron'),
        ),
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
