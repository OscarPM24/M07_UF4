from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def teachers(request):
    return render(request, 'teachers.html')

def students(request):
    return render(request, 'students.html')
