# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-05 05:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_auto_20190403_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('did', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('vehiclenumber', models.CharField(max_length=11)),
                ('status', models.CharField(max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Company')),
            ],
        ),
        migrations.AlterField(
            model_name='resident',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 5, 10, 45, 39, 446109)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 5, 10, 45, 39, 447107)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 5, 10, 45, 39, 449104)),
        ),
        migrations.AddField(
            model_name='delivery',
            name='resident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Resident'),
        ),
    ]
