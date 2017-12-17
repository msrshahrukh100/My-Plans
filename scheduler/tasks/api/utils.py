from ..models import Task, Schedule
from django.utils.timezone import datetime, timedelta

def get_total_percent_data(task, user, dayspast):
	if dayspast :
		schedules = task.schedule.filter(user=user, date__gte=datetime.now()-timedelta(days=dayspast))
	else :
		schedules = task.schedule.filter(user=user)
	success = schedules.filter(status=True).count()
	total = schedules.count()
	if total:
		return float(success*100)/float(total)
	return 0.0

def get_data_of_user(user, dayspast=None):
	data = []
	for task in Task.objects.all() :
		task_data = {
		"name": task.content,
		"percent_completed" : get_total_percent_data(task, user, dayspast),
		"color" : task.color
		}
		data.append(task_data)

	return data


def get_day_record(user, dayspast=0) :
	date = datetime.now()-timedelta(days=dayspast)
	schedules = Schedule.objects.filter(user=user, date=datetime.now()-timedelta(days=dayspast))
	success = schedules.filter(status=True).count()
	total = schedules.count()
	if total:
		return (float(success*100)/float(total), date)
	return (0.0, date)



def get_color_from_score(score):
	if score < 50 :
		return "red darken-4"
	elif score >= 50 and score < 65 :
		return "red darken-2"
	elif score >= 65 and score < 70 :
		return "red lighten-3"
	elif score >= 70 and score < 75:
		return "red lighten-5"
	elif score >=75 and score < 80 :
		return "green lighten-4"
	elif score >= 80 and score < 85:
		return "green lighten-2"
	elif score >= 85 and score < 90:
		return "green"
	elif score >= 90 and score < 93: 
		return "green darken-3"
	elif score >= 93 and score < 95:
		return "green darken-4"
	elif score >= 95 and score < 97:
		return "yellow darken-2"
	elif score >= 97 and score < 99:
		return "yellow darken-3"
	elif score >= 99:
		return "yellow darken-4"


def get_previous_ndays_data(user, ndays=3):
	user = user
	data = []
	if ndays == 0:
		score, date = get_day_record(user, dayspast=0)
		color = get_color_from_score(score)
		data_dict = {"score":int(score), "date":date, "color":color}
		data.append(data_dict)
		return data

	for day in range(1, int(ndays)+1):
		score, date = get_day_record(user, dayspast=day)
		color = get_color_from_score(score)
		data_dict = {"score":int(score), "date":date, "color":color}
		data.append(data_dict)

	return data[::-1]














