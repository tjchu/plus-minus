import datetime
from django.db import models
from django.utils import timezone

class Player(models.Model):
	name_text = models.CharField(max_length=200)
	fga = models.IntegerField(default=0)
	fgm = models.IntegerField(default=0)
	fgp = models.IntegerField(default=0)
	def __str__(self):
		return self.name_text
