from .models import Task


def get_total_percent_data(task, user):
	schedules = task.schedule.filter(user=user)
	success = schedules.filter(status=True).count()
	total = schedules.count()
	if total:
		return float(success*100)/float(total)
	return 0

def get_data_of_user(user):
	columns = [
	        {"id":"","label":"Task","pattern":"","type":"string"},
	        {"id":"","label":"% days accomplished","pattern":"","type":"number"},
	        {"role":"style","type":"string"}
	      ]
	rows = []
	colors = []
	for task in Task.objects.all() :
		colors.append(task.color)
		rows.append({"c":[
			{"v":task.content},
			{"v":get_total_percent_data(task, user)},
			{"v":task.color},
			]})

	data = {
	  "cols": columns,
	  "rows": rows,
	  "colors" : colors,
	  "height" : Task.objects.all().count() * 70
	}
	return data


