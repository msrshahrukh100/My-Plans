# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_timeboundtasks_percent_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeboundtasks',
            name='percent_completed',
            field=models.FloatField(blank=True),
        ),
    ]