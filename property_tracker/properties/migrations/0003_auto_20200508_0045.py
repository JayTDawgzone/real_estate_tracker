# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-08 07:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20200507_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 7, 45, 54, 475991, tzinfo=utc)),
        ),
    ]
