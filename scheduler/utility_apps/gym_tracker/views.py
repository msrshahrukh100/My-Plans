# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserProgramMap
from .forms import ExerciseForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


@login_required
def gym_home(request):
	user = request.user
	user_program, created = UserProgramMap.objects.get_or_create(user=user)
	program = user_program.program
	exercises_for_the_day = program.get_all_excercises_for_the_day()
	if not exercises_for_the_day :
		raise Http404("Excercises for today doesn't exists !")


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
		'number_of_pages': range(1, exercise.paginator.num_pages + 1)}

	return render(request, "gymhome.html", context)