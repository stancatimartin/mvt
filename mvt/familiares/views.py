from asyncio.windows_events import NULL
import re
from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.


def create_familiar(request):
    familiar = Familiares.objects.create(parentesco = 'Primo', nombre = 'Pedro', apellido = 'Perez', hijos = 0)
    context = {
        'nuevo_familiar': familiar
    }
    return render(request, 'nuevo_familiar.html', context=context)

def lista_familiar(request):
    familiares = Familiares.objects.all()
    context = {
        'familiares': familiares
    }
    return render(request, 'lista_familiares.html', context=context) 
