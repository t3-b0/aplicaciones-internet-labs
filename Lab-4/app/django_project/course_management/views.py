from django.shortcuts import render
from .models import Course, Student

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html',{'courses':courses})