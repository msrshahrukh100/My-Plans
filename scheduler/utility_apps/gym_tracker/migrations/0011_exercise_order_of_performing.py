# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_tracker', '0010_auto_20171228_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='order_of_performing',
            field=models.IntegerField(default=1),
        ),
    ]
