from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	last_changed = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=160)
	content = RichTextUploadingField()
	
class Information(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	last_changed = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=160)
	content = RichTextUploadingField()
	
