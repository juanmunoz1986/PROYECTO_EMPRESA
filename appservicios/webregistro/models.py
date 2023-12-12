from django.db import models
from webcrearempresa.models import Empresas
# Create your models here.

class Personas(models.Model):
    PersonaID = models.AutoField(primary_key=True)
    PrimerNombre = models.CharField(max_length=50)
    SegundoNombre = models.CharField(max_length=50)
    PrimerApellido = models.CharField(max_length=50)
    SegundoApellido = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=255)
    Telefono = models.PositiveIntegerField(unique=True)
    FechaNacimiento = models.DateField()
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    FechaModificacion = models.DateTimeField(auto_now=True)
    Email = models.CharField(max_length=50,unique=True)
    NumeroCedula = models.PositiveIntegerField(unique=True)
    Tipousuario = models.CharField(max_length=20)

    def __str__(self):
        return self.PrimerNombre + " " + self.PrimerApellido + " " + str(self.NumeroCedula)


class Clientes(models.Model):
    ClienteID = models.AutoField(primary_key=True)
    PersonaID = models.ForeignKey(Personas, on_delete=models.CASCADE)
    EmpresaID = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    def __str__(self):
        return "Cliente: "+self.PersonaID.PrimerNombre + " " + self.PersonaID.PrimerApellido + " " + self.PersonaID.NumeroCedula
    

class Tecnicos(models.Model):
    TecnicoID = models.AutoField(primary_key=True)
    PersonaID = models.ForeignKey(Personas, on_delete=models.CASCADE)
    def __str__(self):
        return "Tecnico: "+self.PersonaID.PrimerNombre + " " + self.PersonaID.PrimerApellido + " " + self.PersonaID.NumeroCedula
    

class Supervisores(models.Model):
    SupervisorID = models.AutoField(primary_key=True)
    PersonaID = models.ForeignKey(Personas, on_delete=models.CASCADE)
    def __str__(self):
        return "Supervisor: "+self.PersonaID.PrimerNombre + " " + self.PersonaID.PrimerApellido + " " + self.PersonaID.NumeroCedula
    

class Usuarios(models.Model):
    UsuarioID = models.AutoField(primary_key=True)
    PersonaID = models.ForeignKey(Personas, unique=True, on_delete=models.CASCADE)
    NombreUsuario = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=255)
    

