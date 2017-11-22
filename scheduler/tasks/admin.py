# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Task, Schedule, Customizations
from django.contrib import admin

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	list_display = ['content', 'slug', 'order']
	list_editable = ["order"]

class ScheduleManager(admin.ModelAdmin):
	list_display = ['user' ,'date', 'task', 'status']
	list_filter = ['user' ,'date', 'task', 'status']

class CustomizationManager(admin.ModelAdmin):
	list_display = ['color', 'border_color']

admin.site.register(Task, TaskAdmin)
admin.site.register(Schedule, ScheduleManager)
admin.site.register(Customizations, CustomizationManager)
