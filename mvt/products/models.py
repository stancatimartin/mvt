from django.db import models

# Create your models here.

class Products(models.Model):
    type = models.CharField(max_length=40)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()
