from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import UsuariForm
from .models import Usuari

def index(request):
    return render(request, 'index.html')


def teachers(request):
    teachers = Usuari.objects.filter(rol='T')
    return render(request, 'teachers.html', {'teachers': teachers})


def teacher(request, pk):
    teacher = Usuari.objects.get(id=pk)
    return render(request, 'teacher.html', {'teachers': teacher})


def students(request):
    students = Usuari.objects.filter(rol='S')
    return render(request, 'students.html', {'students': students})


def student(request, pk):
    student = Usuari.objects.get(id=pk)
    return render(request, 'student.html', {'students': student})

def user_form(request):
    form = UsuariForm() # Formulari del forms.py

    if request.method == 'POST':
        form = UsuariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    return render(request, 'form.html', context)

def update_user(request, pk):
    usuari = Usuari.objects.get(id=pk)
    form = UsuariForm(instance=usuari)

    if request.method == 'POST':
        form = UsuariForm(request.POST, instance=usuari)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'form.html', context)