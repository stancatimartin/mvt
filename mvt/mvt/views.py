from django.http import HttpResponse
from django.shortcuts import render # sirve para mostrar los html
from datetime import datetime

def saludo(request):
    return HttpResponse('hola, segunda clase con django')

def segundo_template(request):
    today = datetime.today()
    context = {
    'name':'Martin',
    'last_name':'Stancati',
    'today': today
    }
    return render(request, 'template2.html', context=context)

def template_con_lista(request):
    context = {
        'lista': ['tomate', 'naranja', 'banana'],
    }
    return render(request,'template_lista.html', context=context)