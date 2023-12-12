from django.shortcuts import render, redirect
from .models import Equipo, Empresas,Mantenimiento
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from webcrearempresa.models import Empresas
from webregistro.models import Personas
from webregistro.models import Usuarios
from webregistro.models import Clientes
from webregistro.models import Tecnicos
from webregistro.models import Supervisores




def crear_equipos(request):
    
      
    equipos = Equipo.objects.all()
    print(equipos)

    username = request.user.username  # Obtiene el nombre de usuario activo
    
    #en la base de datos webregistro_personas se busca el usuario que esta logueado y se obtiene el id
    persona = Usuarios.objects.get(NombreUsuario=username)

    
    print(persona)
    print (persona.PersonaID_id)
    #con base al id de la persona buscamos en la tabla de personas el tipo de usuario
    persona = Personas.objects.get(PersonaID=persona.PersonaID_id)

    # si el tipo de usuario es cliente se busca en la tabla de clientes el id de la empresa
    if persona.Tipousuario == "cliente":
        cliente = Clientes.objects.get(PersonaID=persona.PersonaID)
        #se filtran los equipos por el id de la empresa
        equipos = Equipo.objects.filter(empresa=cliente.EmpresaID)
        return render(request, "crear_equipos.html", {'equipos': equipos ,'username': username , 'cliente': cliente , 'persona': persona})
        
    # si el tipo de usuario es tecnico se busca en la tabla de tecnicos el id de la persona
    elif persona.Tipousuario == "tecnico":
        tecnico = Tecnicos.objects.get(PersonaID=persona.PersonaID)
        
        #se capturan todos los mtto
        mtto = Mantenimiento.objects.all()

        # se guarda en una lista los equipos que estan en los mtto y estan asignados al tecnico
        equipos = []
        for m in mtto:
            if m.tecnicos == tecnico:
                equipos.append(m.equipo)
        print(equipos)

        #se envian esos equipos en el render
        
        return render(request, "crear_equipos.html", {'equipos': equipos ,'username': username , 'tecnico': tecnico , 'persona': persona})
    
    # si el tipo de usuario es supervisor se busca en la tabla de supervisores el id de la persona
    elif persona.Tipousuario == "supervisor":
        supervisor = Supervisores.objects.get(PersonaID=persona.PersonaID)
        clientes = Empresas.objects.all()
        equipos = Equipo.objects.all()
        return render(request, "crear_equipos.html", {'clientes':clientes , 'equipos': equipos ,'username': username , 'supervisor': supervisor , 'persona': persona})
    # si el usuario no es de ningun tipo se muestra la pagina de inicio
      
    else:  
         return render(request, "crear_equipos.html", {'username': username })


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


def eliminar_equipo(request, equipo_id):
    
    cursos = Equipo.objects.get(id=equipo_id)
    cursos.delete()    
    

    return redirect('crear_equipos')

def editar_equipo(request, equipo_id):
    
    equipo = Equipo.objects.get(id=equipo_id)
    username = request.user.username  # Obtiene el nombre de usuario activo
    clientes = Empresas.objects.all()
    print(clientes)

    return render(request, "editar_equipo.html", {'equipo': equipo ,'username': username , 'clientes': clientes})



def editar(request, equipo_id):
    
    if request.method == "POST":
        id = equipo_id
        nombre = request.POST["nombre"]
        tipo = request.POST["tipo"]
        modelo = request.POST["modelo"]
        serial = request.POST["serial"]
        fecha_mtto = request.POST["fecha_mtto"]
        fecha_calibracion = request.POST["fecha_calibracion"]
        voltaje = request.POST["voltaje"]
        corriente_compresor = request.POST["corriente_compresor"]
        corriente_motor = request.POST["corriente_motor"]            
         
        equipo = Equipo.objects.get(id=id)
        equipo.nombre=nombre
        equipo.tipo=tipo
        equipo.modelo=modelo
        equipo.serial=serial
        equipo.fecha_mtto=fecha_mtto
        equipo.fecha_calibracion=fecha_calibracion
        equipo.voltaje=voltaje
        equipo.corriente_compresor=corriente_compresor
        equipo.corriente_motor=corriente_motor
        
        equipo.save()
        return redirect('crear_equipos')
    else:
        return redirect('crear_equipos')
    

def crear_mtto(request, equipo_id ):

    print('pepito perez')
    equipo = Equipo.objects.get(id=equipo_id)
    username = request.user.username  
    clientes = Empresas.objects.all()
    tecnicos = Tecnicos.objects.all()
    supervisores = Supervisores.objects.all()
    

    print(clientes)
    print('pepito perez')
    return render(request, "crear_mtto.html", {'equipo': equipo ,'username': username , 'clientes': clientes, 'Tecnicos': tecnicos, 'Supervisores': supervisores})
            





def guardar_mmto(request, equipo_id):

    if request.method == "POST":
        id = equipo_id
        observacion = request.POST["observacion"]
        voltage = request.POST["voltaje"]
        corriente_compresor = request.POST["corriente_compresor"]
        corriente_motor = request.POST["corriente_motor"]
        estado = request.POST["estado"]
        tecnico_id = request.POST.get("Tecnicos")
        supervisor_id = request.POST.get("Supervisores")


        print(tecnico_id)
        print(supervisor_id)

       
        
        equipo = Equipo.objects.get(id=id)
        supervisor = Supervisores.objects.get(SupervisorID=supervisor_id)
        tecnico = Tecnicos.objects.get(TecnicoID=tecnico_id)
        cliente = Clientes.objects.get(EmpresaID=equipo.empresa)

        
       

        #se crea el mantenimiento con los datos obtenidos
        # se guarda el mantenimiento
        mantenimiento = Mantenimiento(equipo=equipo, tecnicos=tecnico, supervisor= supervisor)  
        mantenimiento.observacion = observacion 
        mantenimiento.voltage = voltage
        mantenimiento.corriente_compresor = corriente_compresor
        mantenimiento.corriente_motor = corriente_motor
        mantenimiento.estado = estado
        print(mantenimiento)
        mantenimiento.save()
        
        return redirect('crear_equipos')
    else:
        return redirect('crear_equipos')
    


    
    
    
    
    
    
    
   