# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile, UserFRCStreaks
# Register your models here.

class UserFRCStreaksAdmin(admin.ModelAdmin):
	list_display = ['user', 'number_of_times', 'last_day']


admin.site.register(UserProfile)
admin.site.register(UserFRCStreaks, UserFRCStreaksAdmin)
