# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Exercise, Program, ProgramExcerciseMap

# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
	model = Exercise
	list_display = ['exercise_name', 'muscle_group', 'sets', 'reps', 'max_weight']

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program)
admin.site.register(ProgramExcerciseMap)



