# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import EmotionJournalForm
from .models import EmotionJournal
from taggit.models import Tag
from django.http import JsonResponse


# Create your views here.

def get_all_emotions(request):
	emotions_list = list(Tag.objects.values_list('name').distinct())
	emotions = [emotion[0] for emotion in emotions_list]
	return JsonResponse({ "emotions": emotions})

def emotion(request):
	context = {"emotion_journals": EmotionJournal.objects.all().order_by('-id')[:5] }
	if request.method == 'POST':
		emotiontags = request.POST.get('emotiontags')
		if emotiontags :
			tags = [tag.strip() for tag in emotiontags.split(',')]
			context['emotion_journals'] = EmotionJournal.objects.filter(emotions_before__name__in=tags).order_by('-created_at')
		else :
			context['emotion_journals'] = EmotionJournal.objects.all().order_by('-created_at')
	return render(request, "emotion.html", context)

def add_emotion(request):
	form = EmotionJournalForm(request.POST or None)
	context = {"form":form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect("emotionapp:emotion")
	return render(request, "addemotion.html", context)
