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

            if form['rol'].value() == 'T':
                return redirect('teachers')
            elif form['rol'].value() == 'S':
                return redirect('students')

    context = {'form':form}
    return render(request, 'form.html', context)

def update_user(request, pk):
    usuari = Usuari.objects.get(id=pk)
    form = UsuariForm(instance=usuari)

    if request.method == 'POST':
        form = UsuariForm(request.POST, instance=usuari)
        if form.is_valid():
            form.save()

            if usuari.rol == 'T':
                return redirect('teachers')
            elif usuari.rol == 'S':
                return redirect('students')

    context = {'form': form}
    return render(request, 'form.html', context)

def delete_user(request, pk):
    usuari = Usuari.objects.get(id=pk)

    if request.method == 'POST':
        usuari.delete()
        if usuari.rol == 'T':
            return redirect('teachers')
        elif usuari.rol == 'S':
            return redirect('students')

    context = {'object':usuari}
    return render(request, 'delete_object.html', context)