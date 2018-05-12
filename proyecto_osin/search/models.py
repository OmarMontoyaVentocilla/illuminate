#encoding:utf-8
from django.db import models

# Create your models here.
class Auto(models.Model):
    placa=models.CharField(max_length=8,unique=True)
    nombres=models.CharField(max_length=100)
    email=models.EmailField(blank=False)
    descripcion_vida=models.TextField()
    edad=models.IntegerField()
    tiempo_registro=models.DateTimeField(auto_now=True)
    cantidad_dinero=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.nombres

 