# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import EmotionJournalForm
from .models import EmotionJournal, FRCScript
from taggit.models import Tag
from django.http import JsonResponse
from django.db.models import Q

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
			context['emotion_journals'] = EmotionJournal.objects.filter(Q(emotions_before__name__in=tags) | Q(emotions_after__name__in=tags)).order_by('-created_at')
		else :
			context['emotion_journals'] = EmotionJournal.objects.all().order_by('-created_at')
	return render(request, "emotion.html", context)

def add_emotion(request):
	form = EmotionJournalForm(request.POST or None)
	context = {"form":form}
	if request.method == 'POST':
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form.save_m2m()
		return redirect("emotionapp:emotion")
	return render(request, "addemotion.html", context)

def read_frc_scripts(request):
	context = {
	'frc_scripts': FRCScript.objects.all().order_by('created_at')
	}

	return render(request, 'read_frc.html', context)
