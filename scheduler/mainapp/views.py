# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utility_apps.tasks.api.utils import get_previous_ndays_data


# Create your views here.
@login_required()
def home(request):
	context = {
	"ndays_record": get_previous_ndays_data(request.user),
	}
	return render(request, "homepage.html", context)
