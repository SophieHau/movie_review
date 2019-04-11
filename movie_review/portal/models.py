from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
	title = models.CharField(max_length=50)
	year = models.CharField(max_length=4, default=None)
	image = models.TextField()
	plot = models.TextField(default=None, null=True, blank=True)

class Review(models.Model):

	RATINGS = (
		(0, 0),
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
		(7, 7),
		(8, 8),
		(9, 9),
		(10, 10), 
	)

	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('published on')
	rating = models.IntegerField(choices=RATINGS,
                                default=0)

