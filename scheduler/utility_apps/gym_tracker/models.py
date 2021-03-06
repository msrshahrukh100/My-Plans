	# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django.core.files import File
from django.db.models.signals import post_save
import urllib
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Program(models.Model):
	program_name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	number_of_days = models.IntegerField(default=7)

	def __str__(self):
		return self.program_name

	def get_all_excercises_for_the_day(self, days_delta=0):
		day = int(timezone.now().day + days_delta) % self.number_of_days
		day_exercises = self.getexcercises.all().filter(weekday=day).first()
		if day_exercises:
			return (day_exercises, day_exercises.excercises.all().order_by('order_of_performing'))
		else:
			return None, None


class UserProgramMap(models.Model):
	user = models.ForeignKey(User)
	program = models.ForeignKey(Program)

	def __str__(self):
		return str(self.id)


def upload_location(instance, filename):
	return "excercises/%s" %(filename)


class Exercise(models.Model):
	exercise_name = models.CharField(max_length=255)
	muscle_group = models.CharField(max_length=300)
	sets = models.IntegerField(default=1)
	reps = models.IntegerField(default=1)
	max_weight = models.FloatField(default=1)
	image_url = models.URLField(null=True, blank=True)
	image = models.ImageField(upload_to=upload_location, 	
		null=True, 
		blank=True, 
		width_field="width_field", 
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	order_of_performing = models.IntegerField(default=1)
	description = models.TextField()

	def __str__(self):
		return self.exercise_name

	def get_image_url(self):
		if self.image:
			return self.image.url
		return self.image_url



def save_exercise(sender, instance, **kwargs):
	if instance.image_url and not instance.image :
		try:
			result = urllib.urlretrieve(instance.image_url)
			instance.image.save(
			        os.path.basename(instance.image_url),
			        File(open(result[0]))
			        )
		except:
			pass

# uncomment this line when shifting away from pythonanywhere.com
# post_save.connect(save_exercise, sender=Exercise)


class ProgramExcerciseMap(models.Model):
	program = models.ForeignKey(Program, related_name="getexcercises")
	weekday = models.IntegerField(default=1)
	day_of_week = models.CharField(max_length=100, default="Monday")
	day_name = models.CharField(max_length=255, default="Chest Day")
	excercises = models.ManyToManyField(Exercise)

	def __str__(self):
		return str(self.id)

	class Meta:
		ordering = ['weekday']

