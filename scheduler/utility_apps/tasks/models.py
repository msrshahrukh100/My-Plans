# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.



class TimeBoundTasks(models.Model):
	user = models.ForeignKey(User, related_name="timeboundtasks")
	name = models.CharField(max_length=400)
	description = models.TextField()
	unit = models.CharField(max_length=255, help_text="The unit that divides your task into parts. eg in a book of 18 chapters, chapter is the unit")
	total_units = models.FloatField()
	units_completed = models.FloatField(default=0)
	percent_completed = models.FloatField(null=True, blank=True)
	deadline = models.DateTimeField(blank=True, null=True)
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def get_subtasks(self):
		return self.getsubtasks.filter(done=False).order_by('due_date')

	def get_increase_url(self):
		return reverse('tasks:change_tbt_status', kwargs={"id":self.id, "action":"increase"})

	def get_decrease_url(self):
		return reverse('tasks:change_tbt_status', kwargs={"id":self.id, "action":"decrease"})

def add_percent_completed(sender, instance, **kwargs):
	instance.percent_completed = (instance.units_completed / instance.total_units) * 100

pre_save.connect(add_percent_completed, sender=TimeBoundTasks)


class TimeBoundTasksSubtask(models.Model):
	user = models.ForeignKey(User, related_name='tbtsubtasks')
	tbt = models.ForeignKey(TimeBoundTasks, related_name="getsubtasks")
	due_date = models.DateTimeField(null=True, blank=True)
	subtask = models.TextField()
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.subtask

	def is_late(self):
		return self.due_date < timezone.now()

	def get_done_url(self):
		return reverse('tasks:change_tbt_subtask_done', kwargs={'id' : self.id})


class TaskManager(models.Manager):
	def get_queryset(self):
		return super(TaskManager, self).get_queryset().order_by('time')

def get_user():
	return User.objects.first()

class Task(models.Model):
	user = models.ForeignKey(User, default=get_user)
	content = models.TextField()
	slug = AutoSlugField(populate_from='content')
	time = models.DateTimeField()
	color = models.CharField(max_length=255)

	objects = TaskManager()

	def get_task_status(self):
		'''	
			Returns True for active tasks else false
		'''
		if timezone.now() > self.time :
			time_difference = (timezone.now() - self.time).seconds
		else :
			time_difference = (self.time - timezone.now()).seconds

		in_a_difference_of = timezone.timedelta(hours=4).seconds

		if time_difference < in_a_difference_of :
			return True
		return False

	def __str__(self):
		return self.slug

# class ScheduleManager(models.Manager):
# 	def get_queryset(self):
# 		return super(ScheduleManager, self).get_queryset().order_by('date').order_by(self.task.order)

class Schedule(models.Model):
	user = models.ForeignKey(User, related_name="schedules")
	date = models.DateField()
	task = models.ForeignKey(Task, related_name="schedule")
	status = models.BooleanField(default=False)

	def __str__(self):
		return str(self.task)



