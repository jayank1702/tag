# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-01 14:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20190401_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 1, 20, 3, 14, 751890)),
        ),
    ]
