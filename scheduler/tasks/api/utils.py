from ..models import Task


def get_total_percent_data(task, user):
	schedules = task.schedule.filter(user=user)
	success = schedules.filter(status=True).count()
	total = schedules.count()
	if total:
		return float(success*100)/float(total)
	return 0

def get_data_of_user(user):
	data = []
	for task in Task.objects.all() :
		task_data = {
		"name": task.content,
		"percent_completed" : get_total_percent_data(task, user),
		"color" : task.color
		}
		data.append(task_data)
		
	return data


