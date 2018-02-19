
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from taggit.managers import TaggableManager
from taggit.models import Tag, GenericTaggedItemBase
from django.utils.translation import ugettext_lazy as _



# Create your models here.

class Emotions(models.Model):
	name = models.ForeignKey(Tag, related_name="emotion")
	emoticon = models.CharField(max_length=255, blank=True, null=True)
	color = models.CharField(max_length=100, default="none")

	class Meta:
		verbose_name = "Emotions"
		verbose_name_plural = "Emotions"

	def __str__(self):
		return str(self.id)


class TaggedEmotionsBefore(GenericTaggedItemBase):
	tag = models.ForeignKey(Tag, related_name="%(class)s_emotionsbefore")


class TaggedEmotionsAfter(GenericTaggedItemBase):
	tag = models.ForeignKey(Tag, related_name="%(class)s_emotionsafter")


class EmotionJournal(models.Model):

	situation = models.TextField()
	created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	update_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	emotions_before = TaggableManager(blank=True, through=TaggedEmotionsBefore, verbose_name="Emotions Before", help_text="")
	emotions_after = TaggableManager(blank=True,  through=TaggedEmotionsAfter, related_name="emotionsafter", verbose_name="Emotions After", help_text="")

	def __str__(self):
		return str(self.id)


class FRCScript(models.Model):
	trigger = models.TextField()
	face_it_statement = models.TextField()
	replace_it_statement = models.TextField()
	connect_statement = models.TextField()
	created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	update_at = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __str__(self):
		return str(self.id)


# signals are there below this line

def save_emotion(sender, instance, **kwargs):
    obj = Emotions.objects.create(name=instance)
    obj.save()

post_save.connect(save_emotion, sender=Tag)


	