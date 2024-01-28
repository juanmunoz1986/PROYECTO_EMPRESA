from django.db import models
from webcrearempresa.models import Empresas
from webregistro.models import Supervisores, Tecnicos

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
    
class Mantenimiento(models.Model):
    fecha = models.DateField(auto_now_add=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    supervisor = models.ForeignKey(Supervisores, on_delete=models.CASCADE)    
    observacion = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    tecnicos = models.ForeignKey(Tecnicos, on_delete=models.CASCADE)
    voltage = models.CharField(max_length=50)
    corriente_compresor = models.CharField(max_length=50)
    corriente_motor = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    
    def __str__(self):
        return self.equipo.nombre + " " + str(self.fecha)+ " " + self.estado    