# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_movie_user_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(related_name='category_movie', to='catalogo.Category'),
        ),
    ]
