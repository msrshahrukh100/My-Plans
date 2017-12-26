# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class TaskManager(models.Manager):
	def get_queryset(self):
		return super(TaskManager, self).get_queryset().order_by('time')

class Task(models.Model):
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

class ScheduleManager(models.Manager):
	def get_queryset(self):
		return super(ScheduleManager, self).get_queryset().order_by('date').order_by(self.task.order)

class Schedule(models.Model):
	user = models.ForeignKey(User, related_name="schedules")
	date = models.DateField()
	task = models.ForeignKey(Task, related_name="schedule")
	status = models.BooleanField(default=False)

	def __str__(self):
		return str(self.task)



