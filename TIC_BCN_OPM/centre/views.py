from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import UsuariForm
from .models import Usuari

def index(request):
    return render(request, 'index.html')


def teachers(request):
    teachers = [
        {
            'id': 1,
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'correu': 'roger@iticbcn.cat',
            'curs': 'DAM2B',
            'tutor': False,
            'moduls': 'M07'
        },
        {
            'id': 2,
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Bel',
            'correu': 'juanma@iticbcn.cat',
            'curs': 'DAW2A',
            'tutor': True,
            'moduls': 'M06'
        },
        {
            'id': 3,
            'nom': 'Xavi',
            'cognom1': 'Quesada',
            'cognom2': 'Puertas',
            'correu': 'xavi@iticbcn.cat',
            'curs': 'ASIX2A',
            'tutor': False,
            'moduls': 'M08, MAH'
        },
        {
            'id': 4,
            'nom': 'Josep Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'correu': 'oriol@iticbcn.cat',
            'curs': 'DAW2B',
            'tutor': False,
            'moduls': 'M09'
        }
    ]
    return render(request, 'teachers.html', {'teachers': teachers})


def teacher(request, pk):
    teachers = [
        {
            'id': 1,
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'correu': 'roger@iticbcn.cat',
            'curs': 'DAM2B',
            'tutor': False,
            'moduls': 'M07'
        },
        {
            'id': 2,
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Bel',
            'correu': 'juanma@iticbcn.cat',
            'curs': 'DAW2A',
            'tutor': True,
            'moduls': 'M06'
        },
        {
            'id': 3,
            'nom': 'Xavi',
            'cognom1': 'Quesada',
            'cognom2': 'Puertas',
            'correu': 'xavi@iticbcn.cat',
            'curs': 'ASIX2A',
            'tutor': False,
            'moduls': 'M08, MAH'
        },
        {
            'id': 4,
            'nom': 'Josep Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'correu': 'oriol@iticbcn.cat',
            'curs': 'DAW2B',
            'tutor': False,
            'moduls': 'M09'
        }
    ]
    teacher_obj = None
    for i in teachers:
        if i['id'] == pk:
            teacher_obj = i
    return render(request, 'teacher.html', {'teachers': teacher_obj})


def students(request):
    students = [
        {
            'id': 1,
            'nom': 'Oscar',
            'cognom1': 'Perez',
            'cognom2': 'Mengual',
            'correu': 'oscar@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 2,
            'nom': 'Adria',
            'cognom1': 'Garcia',
            'cognom2': 'Perez',
            'correu': 'adria@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 3,
            'nom': 'Gemma',
            'cognom1': 'Garrigosa',
            'cognom2': 'Frances',
            'correu': 'gemma@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 4,
            'nom': 'Facundo Calixto',
            'cognom1': 'Barrios',
            'cognom2': '',
            'correu': 'facundo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 5,
            'nom': 'Angelo',
            'cognom1': 'Montenegro',
            'cognom2': 'Zavala',
            'correu': 'angelo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 6,
            'nom': 'Neus',
            'cognom1': 'Bravo',
            'cognom2': 'Arias',
            'correu': 'neus@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 7,
            'nom': 'Joana Jiayun',
            'cognom1': 'Lin',
            'cognom2': 'Chen',
            'correu': 'joana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 8,
            'nom': 'Veronica',
            'cognom1': 'Cartagena',
            'cognom2': 'Jaldin',
            'correu': 'veronica@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 9,
            'nom': 'Oriana Saray',
            'cognom1': 'Rojas',
            'cognom2': 'Guedez',
            'correu': 'oriana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 10,
            'nom': 'Eric',
            'cognom1': 'Sanchez',
            'cognom2': 'Vazquez',
            'correu': 'eric@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 11,
            'nom': 'Junhong',
            'cognom1': 'Zhu',
            'cognom2': 'Zhang',
            'correu': 'junhong@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 12,
            'nom': 'Alexander',
            'cognom1': 'Andreev',
            'cognom2': 'Apukhtina',
            'correu': 'alexander@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 13,
            'nom': 'Jesus',
            'cognom1': 'Pujada',
            'cognom2': 'Montoya',
            'correu': 'oriana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 14,
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'correu': 'anxo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 15,
            'nom': 'Carlos Andres',
            'cognom1': 'Zambrano',
            'cognom2': 'Aray',
            'correu': 'andres@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 16,
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'correu': 'joel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 17,
            'nom': 'Angel',
            'cognom1': 'Ivanov',
            'cognom2': 'Spasov',
            'correu': 'angel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 18,
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': '',
            'correu': 'dinar@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
    ]
    return render(request, 'students.html', {'students': students})


def student(request, pk):
    students = [
        {
            'id': 1,
            'nom': 'Oscar',
            'cognom1': 'Perez',
            'cognom2': 'Mengual',
            'correu': 'oscar@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 2,
            'nom': 'Adria',
            'cognom1': 'Garcia',
            'cognom2': 'Perez',
            'correu': 'adria@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 3,
            'nom': 'Gemma',
            'cognom1': 'Garrigosa',
            'cognom2': 'Frances',
            'correu': 'gemma@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 4,
            'nom': 'Facundo Calixto',
            'cognom1': 'Barrios',
            'cognom2': '',
            'correu': 'facundo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 5,
            'nom': 'Angelo',
            'cognom1': 'Montenegro',
            'cognom2': 'Zavala',
            'correu': 'angelo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 6,
            'nom': 'Neus',
            'cognom1': 'Bravo',
            'cognom2': 'Arias',
            'correu': 'neus@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 7,
            'nom': 'Joana Jiayun',
            'cognom1': 'Lin',
            'cognom2': 'Chen',
            'correu': 'joana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 8,
            'nom': 'Veronica',
            'cognom1': 'Cartagena',
            'cognom2': 'Jaldin',
            'correu': 'veronica@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 9,
            'nom': 'Oriana Saray',
            'cognom1': 'Rojas',
            'cognom2': 'Guedez',
            'correu': 'oriana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 10,
            'nom': 'Eric',
            'cognom1': 'Sanchez',
            'cognom2': 'Vazquez',
            'correu': 'eric@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 11,
            'nom': 'Junhong',
            'cognom1': 'Zhu',
            'cognom2': 'Zhang',
            'correu': 'junhong@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 12,
            'nom': 'Alexander',
            'cognom1': 'Andreev',
            'cognom2': 'Apukhtina',
            'correu': 'alexander@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 13,
            'nom': 'Jesus',
            'cognom1': 'Pujada',
            'cognom2': 'Montoya',
            'correu': 'oriana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 14,
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'correu': 'anxo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 15,
            'nom': 'Carlos Andres',
            'cognom1': 'Zambrano',
            'cognom2': 'Aray',
            'correu': 'andres@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 16,
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'correu': 'joel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 17,
            'nom': 'Angel',
            'cognom1': 'Ivanov',
            'cognom2': 'Spasov',
            'correu': 'angel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 18,
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': '',
            'correu': 'dinar@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
    ]
    student_obj = None
    for i in students:
        if i['id'] == pk:
            student_obj = i
    return render(request, 'student.html', {'students': student_obj})

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