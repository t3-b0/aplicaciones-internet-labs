from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_now_playing_movies, name="now_playing_movies"),
    path('movies/', views.get_now_playing_movies, name='now_playing_movies')
]