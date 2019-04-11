from django import forms
from django.forms import ModelForm
from .models import Review
from django.utils import timezone
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
	class Meta:
		model = Review
		pub_date = timezone.now()
		fields = ['title', 'text', 'movie', 'pub_date', 'author', 'rating']
		widgets = {'movie': forms.HiddenInput, 'author': forms.HiddenInput}
