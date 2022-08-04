import datetime
from doctest import master
from django.db import models

# Create your models here.

class Familiares(models.Model):
    parentesco = models.CharField(max_length=30, null=True,blank=True)
    nombre = models.CharField(max_length=40, null=True,blank=True)
    apellido = models.CharField(max_length=40, null=True,blank=True)
    hijos = models.IntegerField(null=True,blank=True)
    fechaDeNacimiento = models.DateField(null=True,blank=True)
