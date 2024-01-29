from django.shortcuts import render,redirect
from django.http import HttpResponse



# Create your views here.

def registro_empresa(request):

    #imprimir en consola lo que llegue de el request
    print(request.POST)

    if request.POST:
        nombre = request.POST.get('submit')
        
        if nombre == 'registro_boton':
            return redirect('index.html')
    
    
    return render(request,'registro_empresa.html')