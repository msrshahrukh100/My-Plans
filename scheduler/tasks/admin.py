# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Task, Schedule
from django.contrib import admin

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	list_display = ['content', 'slug', 'time', 'color']
	list_editable = ["time"]

class ScheduleManager(admin.ModelAdmin):
	list_display = ['user' ,'date', 'task', 'status']
	list_filter = ['user' ,'date', 'task', 'status']

class CustomizationManager(admin.ModelAdmin):
	list_display = ['color', 'border_color']
	list_editable = ['border_color']

admin.site.register(Task, TaskAdmin)
admin.site.register(Schedule, ScheduleManager)
