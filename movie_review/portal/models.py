from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
	title = models.CharField(max_length=50)
	year = models.CharField(max_length=4, default=None)
	image = models.TextField()

class Review(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('published on')

