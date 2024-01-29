from django.shortcuts import render, redirect
from .models import Equipo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from webcrearempresa.models import Empresas


def crear_equipos(request):
    
        
    equipos = Equipo.objects.all()
    print(equipos)
    username = request.user.username  # Obtiene el nombre de usuario activo
    clientes = Empresas.objects.all()
    print(clientes)

    

    

    return render(request, "crear_equipos.html", {'equipos': equipos ,'username': username , 'clientes': clientes})


def guardar_equipo(request):

    if request.method == "POST":
        nombre = request.POST["nombre"]
        tipo = request.POST["tipo"]
        modelo = request.POST["modelo"]
        serial = request.POST["serial"]
        fecha_mtto = request.POST["fecha_mtto"]
        fecha_calibracion = request.POST["fecha_calibracion"]
        voltaje = request.POST["voltaje"]
        corriente_compresor = request.POST["corriente_compresor"]
        corriente_motor = request.POST["corriente_motor"]
        empresa = request.POST.get("cliente")
        if empresa == "0":
            return redirect('crear_equipos')
        print("esta es la empresa: "+ empresa)
        
        empresa = Empresas.objects.get(EmpresaID=empresa)
        print(empresa)
        equipo = Equipo(nombre=nombre, tipo=tipo, modelo=modelo, serial=serial, fecha_mtto=fecha_mtto, fecha_calibracion=fecha_calibracion, voltaje=voltaje, corriente_compresor=corriente_compresor, corriente_motor=corriente_motor, empresa=empresa)
        equipo.save()
        return redirect('crear_equipos')
    else:
        return redirect('crear_equipos')
