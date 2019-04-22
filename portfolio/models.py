from django.db import models
from datetime import datetime

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(default=datetime.now, blank=True)
	thumb = models.ImageField(default='default.png', blank=True)
	urlDemo = models.URLField(null=True, blank=True)
	urlGit = models.URLField(null=True, blank=True)



	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:300] + '...'