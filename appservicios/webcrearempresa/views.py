from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Empresas
from django.db import models
from datetime import datetime



# Create your views here.

def registro_empresa(request):

    #imprimir en consola lo que llegue de el request
    print(request.POST)

    if request.POST:
        #obtener datos del formulario
        nombre_empresa = request.POST.get('NombreEmpresa')
        nit = request.POST.get('Nit')
        direccion = request.POST.get('Domicilio')
        telefono = request.POST.get('Telefono')
        fecha_creacion = datetime.now()
        fecha_modificacion = datetime.now()

       
        empresa = Empresas()
        #asignar valores a los atributos del objeto
        empresa.NombreEmpresa = nombre_empresa
        empresa.nit = nit
        empresa.DireccionEmpresa = direccion
        empresa.telefono = telefono  
        empresa.FechaCreacion = fecha_creacion
        empresa.FechaModificacion = fecha_modificacion       
        
        #guardar el objeto en la base de datos
        empresa.save()
        #redireccionar a la pagina de inicio
        return redirect('/')
    
    else:
        return render(request,'registro_empresa.html')



        
    
    
