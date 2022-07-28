from django.contrib import admin
from django.urls import path
#from mvt.views import saludo, segundo_template, template_con_lista
from familiares.views import create_familiar, lista_familiar
urlpatterns = [
    path('admin/', admin.site.urls),
#    path('saludo/', saludo, name='saludo'),
#    path('segundo_template/', segundo_template, name= 'segundo_template'),
#    path('template_con_lista/', template_con_lista, name= 'template_con_lista'),
    path('create_familiar/', create_familiar, name= 'create_familiar'),
    path('lista_familiar/', lista_familiar, name= 'lista_familiar')
    ]
