# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-29 15:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20190329_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 29, 20, 58, 48, 48130)),
        ),
    ]