# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Service(models.Model):

	name = models.CharField(max_length=100, default='')
	description = models.TextField(default='')
	cost = models.IntegerField(default=0)
	type = models.CharField(max_length=500, default='')
	image = models.CharField(max_length=50, default='')
	image_num = models.IntegerField(default=0)

	def __str__(self):
		return self.name


