# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_tracker', '0002_exercise_muscle_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='reps',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets',
            field=models.IntegerField(default=1),
        ),
    ]
