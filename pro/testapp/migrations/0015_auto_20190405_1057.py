# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-05 05:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0014_auto_20190405_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 5, 10, 57, 17, 483874)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 5, 10, 57, 17, 484871)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 5, 10, 57, 17, 484871)),
        ),
    ]
