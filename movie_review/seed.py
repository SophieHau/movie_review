from faker import Faker
from imdb import IMDb
from portal.models import Movie, Review
from django.utils import timezone
from django.contrib.auth.models import User
import random


ia = IMDb('http')
fake = Faker()

top = ia.get_top250_movies() [1:11]



def generate_movie_object():
	for movie in top:
		ia.update(movie)
		m = Movie(title=movie['title'], year=movie['year'], image=movie['cover'], plot=movie['plot'])
		m.save()



def generate_review():
	for i in range(0, 31):
		movie = random.choice(Movie.objects.all())
		title = fake.text(30)
		text = fake.text(350)
		author = random.choice(User.objects.all())
		pub_date = timezone.now()
		rating = random.randint(0, 10)
		r = Review(movie=movie, title=title, text=text, author=author, pub_date=pub_date, rating=rating)
		r.save()

def generate_user():
	first_name = fake.first_name()
	last_name = fake.last_name()
	username = first_name[0]+ '_' + last_name
	email = first_name + '.' + last_name + '@' + 'moviereview.com'
	password = fake.password()
	user = User.objects.create_user(username, email, password)
	user.save()
