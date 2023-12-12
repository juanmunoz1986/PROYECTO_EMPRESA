from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.



def index(request):

    username = request.user.username  # Obtiene el nombre de usuario activo

    return render(request, 'index.html', {'username': username})




def cerrar_sesion(request):
    # Cierra la sesión del usuario
    logout(request)
    # Redirige al index o a la página de inicio de sesión
    return redirect('../')