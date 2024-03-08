from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def teachers(request):
    users = [
        {
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'correu': 'roger@iticbcn.cat',
            'curs': 'DAM2B',
            'moduls': 'M07'
        },
        {
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Bel',
            'correu': 'juanma@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06'
        },
        {
            'nom': 'Xavi',
            'cognom1': 'Quesada',
            'cognom2': 'Puertas',
            'correu': 'xavi@iticbcn.cat',
            'curs': 'ASIX2A',
            'moduls': 'M08, MAH'
        },
        {
            'nom': 'Josep Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'correu': 'oriol@iticbcn.cat',
            'curs': 'DAW2B',
            'moduls': 'M09'
        }
    ]
    context = {'users': users}
    return render(request, 'teachers.html', context)

def students(request):
    users = [
        {
            'nom': 'Oscar',
            'cognom1': 'Perez',
            'cognom2': 'Mengual',
            'correu': 'oscar@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Adria',
            'cognom1': 'Garcia',
            'cognom2': 'Perez',
            'correu': 'adria@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Gemma',
            'cognom1': 'Garrigosa',
            'cognom2': 'Frances',
            'correu': 'gemma@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Facundo',
            'cognom1': 'Barrios',
            'cognom2': '',
            'correu': 'facundo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Angelo',
            'cognom1': 'Montenegro',
            'cognom2': 'Zavala',
            'correu': 'angelo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Neus',
            'cognom1': 'Bravo',
            'cognom2': 'Arias',
            'correu': 'neus@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Joana',
            'cognom1': 'Lin',
            'cognom2': 'Chen',
            'correu': 'joana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Veronica',
            'cognom1': 'Cartagena',
            'cognom2': 'Jaldin',
            'correu': 'veronica@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        },
        {
            'nom': 'Oriana',
            'cognom1': 'Rojas',
            'cognom2': 'Guedez',
            'correu': 'oriana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'tots'
        }
    ]
    context = {'users': users}
    return render(request, 'students.html', context)
