from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.

class Article(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	last_changed = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=160)
	content = RichTextUploadingField()

	def __str__(self):
		return "{}: {}".format(self.last_changed, self.title)
	
class Information(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	last_changed = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=160)
	content = RichTextUploadingField()

	def __str__(self):
		return "{}: {}".format(self.last_changed, self.title)
	
class PhotoTag(models.Model):
	name = models.CharField(max_length=40, unique = True)

	def __str__(self):
		return self.name

class Photo(models.Model):
	image = models.ImageField(upload_to='gallery/')
	image_thumbnail = ImageSpecField(source='image',
									processors=[ResizeToFit(100, 100)],
									format='JPEG',
									options={'quality': 60})
	image_show = ImageSpecField(source='image',
								processors=[ResizeToFit(1024, 800)],
								format='JPEG',
								options={'quality': 60})
	tags = models.ManyToManyField(PhotoTag)

	def __str__(self):
		return "[PHOTO] [{}]".format(", ".join(str(t) for t in self.tags.all()))
	
