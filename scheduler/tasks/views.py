# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Schedule, Task
from django.utils.timezone import datetime


# Create your views here.
@login_required
def home(request):

	plans = Schedule.objects.filter(user=request.user, date=datetime.today())
	if not plans.exists():
		for task in Task.objects.all():
			Schedule.objects.create(user=request.user, date=datetime.today(), task=task)
		plans = Schedule.objects.filter(user=request.user, date=datetime.today())

	context = {
	"plans": plans,
	"date" : datetime.today()
	}
	return render(request, "index.html", context)

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


def history(request):
	plans = Schedule.objects.all()
	context = {"plans": plans}
	return render(request, "history.html", context)
