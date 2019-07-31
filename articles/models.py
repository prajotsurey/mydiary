from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length = 50)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey( User, default = None, on_delete = 'PROTECT')
	image = models.ImageField(default = "default.jpg" , blank = True)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:100]+"..."
