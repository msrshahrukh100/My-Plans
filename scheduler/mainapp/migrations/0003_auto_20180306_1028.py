# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-06 04:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_userfrcstreaks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfrcstreaks',
            name='last_day',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 4, 58, 40, 550946, tzinfo=utc)),
        ),
    ]
