# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20171219_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]