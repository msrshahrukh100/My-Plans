# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20171219_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
