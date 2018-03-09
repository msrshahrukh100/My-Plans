# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserProgramMap
from .forms import ExerciseForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
# Create your views here.


@login_required
def change_days_delta(request, action="increase"):
	if action == "increase":
		delta = request.session.get("days_delta", 0)
		delta += 1
		request.session["days_delta"] = delta
		return JsonResponse({'msg': 'Increased'})
	elif action == "decrease":
		delta = request.session.get("days_delta", 0)
		delta -= 1
		request.session["days_delta"] = delta
		return JsonResponse({'msg': 'Decreased'})



@login_required
def gym_home(request):
	user = request.user
	days_delta = request.session.get('days_delta')

	user_program, created = UserProgramMap.objects.get_or_create(user=user)
	program = user_program.program
	if days_delta:
		program_exercise_map_object, exercises_for_the_day = program.get_all_excercises_for_the_day(days_delta=days_delta)
	else:
		program_exercise_map_object, exercises_for_the_day = program.get_all_excercises_for_the_day()
	if not exercises_for_the_day :
		context = {
		'day': "No exercises for today exists"
		}
		return render(request, "gymhome.html", context)


	paginator = Paginator(exercises_for_the_day, 1)

	page = request.GET.get('page')

	try:
		exercise = paginator.page(page)

	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
		exercise = paginator.page(1)

	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
		exercise = paginator.page(paginator.num_pages)

	instance = exercise.object_list[0]
	form = ExerciseForm(request.POST or None, instance = instance)

	if request.method == 'POST':
		print 
		if form.is_valid():
			form.save()

	context = {
		'form': form,
		'exercise' : exercise,
		'instance': instance,
		'day_of_week': program_exercise_map_object.day_of_week,
		'day': program_exercise_map_object.day_name,
		'number_of_pages': range(1, exercise.paginator.num_pages + 1)}

	return render(request, "gymhome.html", context)