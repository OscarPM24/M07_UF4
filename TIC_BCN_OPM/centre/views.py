from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import UsuariForm
from .models import Usuari

def index(request):
    return render(request, 'index.html')


def teachers(request):
    teachers = Usuari.objects.filter(rol='T') # Agafem tots els usuaris filtrats per rol Teacher
    return render(request, 'teachers.html', {'teachers': teachers})


def teacher(request, pk):
    teacher = Usuari.objects.get(id=pk) # Agafem el usuari amb la id pasada per paràmetre
    return render(request, 'teacher.html', {'teachers': teacher})


def students(request):
    students = Usuari.objects.filter(rol='S')# Agafem tots els usuaris filtrats per rol Student
    return render(request, 'students.html', {'students': students})


def student(request, pk):
    student = Usuari.objects.get(id=pk) # Agafem el usuari amb la id pasada per paràmetre
    return render(request, 'student.html', {'students': student})

def user_form(request):
    form = UsuariForm() # Formulari del forms.py

    if request.method == 'POST':
        form = UsuariForm(request.POST)
        if form.is_valid():
            form.save() # Guardem les dades

            if form['rol'].value() == 'T': # Si el usuari es profesor
                return redirect('teachers')
            elif form['rol'].value() == 'S': # Si el usuari es alumne
                return redirect('students')

    context = {'form':form}
    return render(request, 'form.html', context) # Anem a la template form

def update_user(request, pk):
    usuari = Usuari.objects.get(id=pk) # Agafem el usuari amb la id pasada per paràmetre
    form = UsuariForm(instance=usuari) # Agafem el formulari amb les dades del usuari

    if request.method == 'POST':
        form = UsuariForm(request.POST, instance=usuari)
        if form.is_valid():
            form.save() # Guardem les dades

            if usuari.rol == 'T':  # Si el usuari es profesor
                return redirect('teachers')
            elif usuari.rol == 'S':  # Si el usuari es alumne
                return redirect('students')

    context = {'form': form}
    return render(request, 'form.html', context) # Anem a la template form

def delete_user(request, pk):
    usuari = Usuari.objects.get(id=pk) # Agafem el usuari amb la id pasada per paràmetre

    if request.method == 'POST':
        usuari.delete() # Esborrem les dades

        if usuari.rol == 'T': # Si el usuari es profesor
            return redirect('teachers')
        elif usuari.rol == 'S': # Si el usuari es alumne
            return redirect('students')

    context = {'object':usuari}
    return render(request, 'delete_object.html', context) # Anem a la template delete_object