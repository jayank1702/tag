# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-08 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0020_auto_20190408_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 8, 12, 38, 43, 271378)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 8, 12, 38, 43, 272375)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 8, 12, 38, 43, 273373)),
        ),
    ]
