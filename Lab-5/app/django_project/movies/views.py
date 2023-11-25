from django.http import JsonResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def get_genres(request):
    response = requests.get('http://api.filmon.com/api/vod/genres')
    genres = response.json()
    return JsonResponse(genres)

def get_movies(request):
    genre_id = request.GET.get('genre')
    response = requests.get(f'http://api.filmon.com/api/vod/search?genre={genre_id}')
    movies = response.json()
    return JsonResponse(movies)