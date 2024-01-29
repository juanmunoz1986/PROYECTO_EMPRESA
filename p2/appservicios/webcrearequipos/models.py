from django.db import models
from webcrearempresa.models import Empresas

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    fecha_mtto = models.DateField()
    fecha_calibracion = models.DateField()
    voltaje = models.CharField(max_length=50)
    corriente_compresor = models.CharField(max_length=50)
    corriente_motor = models.CharField(max_length=50)   
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)

    


    def __str__(self):
        return self.nombre