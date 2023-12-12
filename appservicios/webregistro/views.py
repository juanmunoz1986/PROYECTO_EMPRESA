from django.shortcuts import render, redirect
from .forms import PersonasForm, UsuariosForm, ClientesForm
from .models import Clientes, Tecnicos, Supervisores
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from webcrearempresa.models import Empresas


def registro(request):
    clientes = Empresas.objects.all()
    if request.method == 'POST':
        form = PersonasForm(request.POST)  # Recibe los datos de la persona
        form2 = UsuariosForm(request.POST)  # Recibe los datos del usuario
        
      

        #imprimir en consala los datos recibido en form2
        

        if form.is_valid():
            # Guarda la persona
            persona = form.save()            
            # Asigna la persona al usuario y guárdalo
            usuario = form2.save(commit=False)
            usuario.PersonaID = persona  # Asigna la persona al usuario
            # capturar el tipo de usuario de form2
            tipo_usuario = form.cleaned_data['Tipousuario']
            # si el usuario es de tipo supervisor guarda el campo SupervisorID
            if tipo_usuario == 'supervisor':
                               
                supervisor = Supervisores(PersonaID = persona)
                supervisor.save()
            # si el usuario es de tipo tecnico guarda el campo TecnicoID
            elif tipo_usuario == 'tecnico':
                
                tecnico = Tecnicos(PersonaID = persona)
                tecnico.save()
            
            elif tipo_usuario == 'cliente':

                empresa = request.POST.get("cliente")
                print("esta es la empresa: "+ empresa)
                empresa = Empresas.objects.get(EmpresaID=empresa)
                cliente = Clientes(PersonaID = persona, EmpresaID = empresa)                
                cliente.save()

            

            username = form2.cleaned_data['NombreUsuario']  # Asegúrate de que el formulario tenga un campo 'username'
            password = form2.cleaned_data['Contraseña']  # Asegúrate de que el formulario tenga un campo 'password'            
            user = User.objects.create_user(username=username, password=password)
            user.is_staff = True
            # que el susuario sea guardado como parte del staff
            
            usuario.User = user  # Asigna el usuario a la instancia de usuario
            usuario.save()



            return redirect('../')

            # Aquí puedes redirigir a la página que desees después de guardar los datos

    else:
        form = PersonasForm()
        form2 = UsuariosForm()
        

    return render(request, 'crear_persona.html', {'form': form, 'form2': form2 , 'clientes': clientes})


def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../')  # Reemplaza 'pagina_de_inicio' con la URL de tu página de inicio
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
