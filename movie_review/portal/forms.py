from django import forms
from django.forms import ModelForm
from .models import Review
from django.utils import timezone

class ReviewForm(ModelForm):
	movie = forms.HiddenInput()
	pub_date = timezone.now()
	class Meta:
		model = Review
		fields = ['title', 'text', 'movie', 'pub_date', 'author']
