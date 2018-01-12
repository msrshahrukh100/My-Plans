# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Schedule, Task, TimeBoundTasks, TimeBoundTasksSubtask
from django.utils.timezone import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from api.utils import get_data_of_user, get_previous_ndays_data, get_color_from_score

# Create your views here.
@login_required(login_url='admin/')
def home(request):

	plans = Schedule.objects.filter(user=request.user, date=datetime.today())
	if not plans.exists():
		for task in Task.objects.all():
			Schedule.objects.create(user=request.user, date=datetime.today(), task=task)
		plans = Schedule.objects.filter(user=request.user, date=datetime.today())

	context = {
	"ndays_record": get_previous_ndays_data(request.user),
	"plans": plans,
	"date" : datetime.today()
	}
	return render(request, "index.html", context)

@login_required()
def time_bound_tasks(request):
	user = request.user
	context = {"tbts": TimeBoundTasks.objects.filter(user=user)}
	return render(request, "timebound.html", context)

def change_tbt_subtask_done(request, id):
	subtask = get_object_or_404(TimeBoundTasksSubtask, id=id)
	subtask.done = True
	subtask.save()

	return redirect('tasks:time_bound_tasks')



def change_tbt_status(request, id, action):
	user = request.user
	tbt = get_object_or_404(TimeBoundTasks, id=id, user=user)
	if action == "increase" :
		if tbt.units_completed < tbt.total_units :
			tbt.units_completed = tbt.units_completed + 1
			tbt.save()
			return JsonResponse({"msg": "Progress Made",
				"id": id,
				"units_completed": tbt.units_completed,
				"percent_completed": float("{:.2f}".format(tbt.percent_completed)),
				"color": get_color_from_score(tbt.percent_completed)
				})
		else:
			return JsonResponse({"msg": "You completed this!!"})
	elif action == "decrease" :
		if tbt.units_completed > 0 :
			tbt.units_completed = tbt.units_completed - 1
			tbt.save()
			return JsonResponse({"msg": "Decreased",
				"id": id,
				"units_completed": tbt.units_completed,
				"percent_completed": float("{:.2f}".format(tbt.percent_completed)),
				"color": get_color_from_score(tbt.percent_completed)
				})
		else :
			return JsonResponse({"msg": "Cannot decrease"})
	return JsonResponse({"msg":"Error"})


def history(request):
	plans = Schedule.objects.all()
	context = {
	"ndays_record": get_previous_ndays_data(request.user),
	"plans": plans,
	}
	return render(request, "history.html", context)


def analysis(request):
	context = {
	"ndays_record": get_previous_ndays_data(request.user),
	"user_data_past_day" : get_data_of_user(request.user, dayspast=1),
	"user_data_past_week" : get_data_of_user(request.user, dayspast=7),
	"user_data_past_month" : get_data_of_user(request.user, dayspast=30),
	"user_data_forever" : get_data_of_user(request.user)
	}
	return render(request, "analysis.html", context)


@login_required
def change_status(request, id=None):
	plan = get_object_or_404(Schedule, user=request.user, id=id)
	if plan.status :
		plan.status = False
		plan.save()
		return JsonResponse({'msg': "Task Undone!"})
	else :
		plan.status = True
		plan.save()
		return JsonResponse({'msg': "Marked Done!"})
	
def get_todays_score(request):
	return JsonResponse ({"data":get_previous_ndays_data(request.user, 0)})

class AnalysisData(APIView):

    def get(self, request, format=None):
		return Response(get_data_of_user(request.user))

