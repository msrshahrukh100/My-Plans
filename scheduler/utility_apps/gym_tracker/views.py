# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserProgramMap
from .forms import ExerciseForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def gym_home(request):
	user = request.user
	program = UserProgramMap.objects.get(user=user).program
	exercises_for_the_day = program.get_all_excercises_for_the_day()

	form = ExerciseForm(request.POST or None, instance = exercises_for_the_day.first())

	if request.method == 'POST':
		if form.is_valid():
			obj = form.save()
			print obj.sets
			print obj.reps
			print obj.max_weight
			print obj.exercise_name

	context = {"form": form}

	# paginator = Paginator(exercises_for_the_day, 25) # Show 25 contacts per page

	# page = request.GET.get('page')
	# try:
	#     contacts = paginator.page(page)
	# except PageNotAnInteger:
	#     # If page is not an integer, deliver first page.
	#     contacts = paginator.page(1)
	# except EmptyPage:
	#     # If page is out of range (e.g. 9999), deliver last page of results.
	#     contacts = paginator.page(paginator.num_pages)

	# return render(request, 'list.html', {'contacts': contacts})


	return render(request, "gymhome.html", context)