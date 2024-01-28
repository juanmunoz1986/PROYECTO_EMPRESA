from django.db import models

# Create your models here.

class Empresas(models.Model):
    EmpresaID = models.AutoField(primary_key=True)
    NombreEmpresa = models.CharField(max_length=255)
    DireccionEmpresa = models.CharField(max_length=255)
    nit= models.CharField(max_length=255)
    FechaCreacion = models.DateTimeField()
    FechaModificacion = models.DateTimeField()
    telefono = models.CharField(max_length=255)