from .models import Task
from .models import Customizations

{"labels" : [],
        "values" : [],
        "color" : [],
        "border_color" : [] }

def get_total_percent_data(task, user):
	schedules = task.schedule.filter(user=user)
	success = schedules.filter(status=True).count()
	total = schedules.count()
	if total:
		return float(success*100)/float(total)
	return 0

def get_data_of_user(user):
	labels = []
	values = []
	customize = Customizations.objects.all()[:Task.objects.all().count()]
	color = [c.color for c in customize]
	border_color = [c.border_color for c in customize]
	for task in Task.objects.all() :
		labels.append(task.content)
		values.append(get_total_percent_data(task, user))

	data = {"labels" : labels, 
	"values" : values,
	"color" : color,
	"border_color" : border_color}
	return data


