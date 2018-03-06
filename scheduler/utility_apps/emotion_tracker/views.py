# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import EmotionJournalForm
from .models import EmotionJournal, FRCScript
from taggit.models import Tag
from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone
from mainapp.models import UserFRCStreaks

# Create your views here.


def get_all_emotions(request):
	emotions_list = list(Tag.objects.values_list('name').distinct())
	emotions = [emotion[0] for emotion in emotions_list]
	return JsonResponse({"emotions": emotions})


def emotion(request):
	context = {
		"emotion_journals": EmotionJournal.objects.all().order_by('-id')[:5]
	}
	if request.method == 'POST':
		emotiontags = request.POST.get('emotiontags')
		if emotiontags:
			tags = [tag.strip() for tag in emotiontags.split(',')]
			context['emotion_journals'] = EmotionJournal.objects.filter(
				Q(emotions_before__name__in=tags) |
				Q(emotions_after__name__in=tags)).order_by('-created_at')
		else:
			context['emotion_journals'] = EmotionJournal.objects.all().order_by('-created_at')
	return render(request, "emotion.html", context)


def add_emotion(request):
	form = EmotionJournalForm(request.POST or None)
	context = {"form": form}
	if request.method == 'POST':
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form.save_m2m()
		return redirect("emotionapp:emotion")
	return render(request, "addemotion.html", context)


def read_frc_scripts(request):
	context = {
		'frc_scripts': FRCScript.objects.all().order_by('-created_at')
	}

	return render(request, 'read_frc.html', context)


def increase_streak(streak_obj):
	streak_obj.number_of_times += 1
	streak_obj.save()


def frc_scripts_streak(request):

	user = request.user
	times_user_does_frc = user.userprofile.first().frc_times
	frc_streaks = request.session.get('frc_streaks')
	streak_obj, created = UserFRCStreaks.objects.get_or_create(
		user=user,
		last_day__date=timezone.now().date())
	streak_count = UserFRCStreaks.objects.get_user_current_streak(user)
	if created:
		request.session["frc_streaks"] = []
		frc_streaks = []

	if not frc_streaks:
		request.session["frc_streaks"] = [timezone.now().day]
		streak_obj.number_of_times = 1
		streak_obj.save()
		return JsonResponse({
			"status": '1',
			"msg": "A new streak count added ",
			"streak_count": streak_count,
			"today_times": "You did it " + str(streak_obj.number_of_times) + " times today",
			})
	else:
		if len(frc_streaks) == times_user_does_frc - 1:
			frc_streaks.append(timezone.now().day)
			request.session["frc_streaks"] = frc_streaks
			increase_streak(streak_obj)
			return JsonResponse({
				"status": '2',
				"msg": "Day streak completed ",
				"streak_count": streak_count,
				"today_times": "You did it " + str(streak_obj.number_of_times) + " times today",
				})
		elif len(frc_streaks) > times_user_does_frc - 1:
			increase_streak(streak_obj)
			return JsonResponse({
				"status": '2',
				"msg": "You are doing great !! You did more than your set goals !! ",
				"streak_count": streak_count,
				"today_times": "You did it " + str(streak_obj.number_of_times) + " times today",
				})
		else:
			frc_streaks.append(timezone.now().day)
			request.session["frc_streaks"] = frc_streaks
			increase_streak(streak_obj)
			return JsonResponse({
				"status": '1',
				"msg": "New Day streak added ",
				"streak_count": streak_count,
				"today_times": "You did it " + str(streak_obj.number_of_times) + " times today",
				})
