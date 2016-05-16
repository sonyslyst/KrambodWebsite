from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	last_changed = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=160)
	content = models.CharField(max_length=1024)
	
class Informasjon(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	last_changed = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=160)
	content = models.CharField(max_length=1024)
	
