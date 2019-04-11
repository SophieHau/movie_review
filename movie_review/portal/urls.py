from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('', views.index, name='index'),
	path('movies/<int:movie_id>', views.show_movie, name='show_movie'),
	path('reviews/<int:review_id>', views.show_review, name='show_review'),
	path('reviews/add/<int:movie_id>', views.add_review, name='add_review'),
	path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(
		template_name='registration/logout.html'), name='logout'),
]