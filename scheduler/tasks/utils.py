from .models import Task
from .models import Customizations


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
	        {"id":"","label":"% days accomplished","pattern":"","type":"number"}
	      ]
	rows = []
	customize = Customizations.objects.all()[:Task.objects.all().count()]
	color = [c.color for c in customize]
	border_color = [c.border_color for c in customize]
	for task in Task.objects.all() :
		rows.append({"c":[{"v":task.content,"f":None},{"v":get_total_percent_data(task, user),"f":None}]})

	data = {
	  "cols": columns,
	  "rows": rows
	}
	return data


