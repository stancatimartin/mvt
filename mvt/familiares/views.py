from asyncio.windows_events import NULL
from django.shortcuts import render
from familiares.models import Familiares
from datetime import datetime, timedelta

# Create your views here.


def create_familiar(request):
    familiar = Familiares.objects.create(parentesco = 'Sobrino', nombre = 'Pepe', apellido = 'Suarez', hijos = 0, fechaDeNacimiento = '1999-5-3')
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
