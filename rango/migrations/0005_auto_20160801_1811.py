# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20160801_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=NameError),
        ),
    ]
