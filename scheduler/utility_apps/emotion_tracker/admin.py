# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import EmotionJournal, Emotions, FRCScript

# Register your models here.

class EmotionsAdmin(admin.ModelAdmin):
	list_display = ['name' ,'emoticon', 'color']
	list_editable = ['emoticon', 'color']


admin.site.register(EmotionJournal)
admin.site.register(Emotions, EmotionsAdmin)
admin.site.register(FRCScript)
