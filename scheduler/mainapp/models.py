# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
	user = models.ForeignKey(User, related_name='userprofile')
	frc_times = models.IntegerField(default=0, help_text="The number of times you are doing FRCs in a day")

	def __str__(self):
		return str(self.user.username)


class UserFRCStreaksManager(models.Manager):
	def get_user_current_streak(self, user):
		query_set = super(UserFRCStreaksManager, self).get_queryset().filter(user=user).order_by('last_day')
		dates_done = []
		streak_count = 0
		for index, query in enumerate(query_set):
			if index < query_set.count() - 1:
				date_delta = query_set[index + 1].last_day - query.last_day
				if date_delta.days == 1:
					dates_done.append(1)
				else:
					dates_done.append(0)
		for i in dates_done[::-1]:
			if i == 1:
				streak_count += 1
			else:
				break
		return streak_count + 1


class UserFRCStreaks(models.Model):
	user = models.ForeignKey(User, related_name='userfrcstreaks')
	number_of_times = models.IntegerField(default=0, help_text="The number of times you are doing FRCs in a day")
	last_day = models.DateTimeField(default=timezone.now())

	objects = UserFRCStreaksManager()

	def __str__(self):
		return str(self.user.username)
