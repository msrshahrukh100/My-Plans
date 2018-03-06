# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import (Task, Schedule, TimeBoundTasks, TimeBoundTasksSubtask, Aims, Timeline)
from django.contrib import admin


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	list_display = ['content', 'slug', 'time', 'color']
	list_editable = ['color']

class ScheduleManager(admin.ModelAdmin):
	list_display = ['user' ,'date', 'task', 'status']
	list_filter = ['user' ,'date', 'task', 'status']

class TimeBoundTasksAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'unit', 'total_units', 'units_completed', 'deadline', 'completed']
	list_filter = ['completed']

class TimeBoundTasksSubtaskAdmin(admin.ModelAdmin):
	list_display = ['user', 'tbt', 'due_date', 'subtask']


class TimelineAdmin(admin.ModelAdmin):
	list_display = ["text", "date"]


admin.site.register(Task, TaskAdmin)
admin.site.register(Schedule, ScheduleManager)
admin.site.register(TimeBoundTasks, TimeBoundTasksAdmin)
admin.site.register(TimeBoundTasksSubtask, TimeBoundTasksSubtaskAdmin)
admin.site.register(Aims)
admin.site.register(Timeline, TimelineAdmin)