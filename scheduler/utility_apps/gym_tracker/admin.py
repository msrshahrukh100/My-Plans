# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Exercise, Program, ProgramExcerciseMap, UserProgramMap

# Register your models here.


class ExerciseAdmin(admin.ModelAdmin):
	model = Exercise
	list_display = ['exercise_name', 'muscle_group', 'sets', 'reps', 'max_weight', 'order_of_performing']
	list_editable = ['order_of_performing']
	list_filter = ['muscle_group']


class ProgramExerciseMapAdmin(admin.ModelAdmin):
	model = ProgramExcerciseMap
	list_display = ['program', 'day_name', 'day_of_week', 'weekday']
	list_editable = ['day_name', 'weekday', 'day_of_week']


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program)
admin.site.register(ProgramExcerciseMap, ProgramExerciseMapAdmin)
admin.site.register(UserProgramMap)
