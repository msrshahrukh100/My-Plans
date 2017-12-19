# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import EmotionJournal, Emotions

# Register your models here.

admin.site.register(EmotionJournal)
admin.site.register(Emotions)
