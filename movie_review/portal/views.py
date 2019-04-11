from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
	movies = Movie.objects.all()
	return render(request, 'index.html', {
			'movies': movies
		})

def show_movie(request, movie_id):
	movie = Movie.objects.get(pk=movie_id)
	reviews = Review.objects.order_by('-pub_date').filter(movie_id=movie_id)
	return render(request, 'show_movie.html', {
			'movie': movie,
			'reviews': reviews
		})

def show_review(request, review_id):
	review = Review.objects.get(pk=review_id)
	return render(request, 'show_review.html', {
			'review':review
		})

def add_review(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	pub_date = timezone.now()
	f = ReviewForm(initial={'movie':movie, 'pub_date': pub_date})
	if request.method == 'POST':
		f = ReviewForm(request.POST)
		print(f)
		if f.is_valid():
			f.save()
			return redirect('show_movie', movie_id=movie_id)
		print(f)
	return render(request, 'add_review.html', {
			'form': f,
			'movie': movie
		})