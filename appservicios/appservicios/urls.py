"""
URL configuration for appservicios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webregistro.views import registro,login1
from WebInicio.views import cerrar_sesion
from webcrearempresa.views import registro_empresa
from WebInicio.views import index
from webcrearequipos.views import crear_equipos, guardar_equipo, eliminar_equipo, editar_equipo, editar, crear_mtto, guardar_mmto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registro_empresa/', registro_empresa),
    path('registro/', registro),
    path('login/', login1),
    path('cerrarsesion/', cerrar_sesion, name='cerrar_sesion'),
    path('crear_equipos/', crear_equipos, name='crear_equipos'),
    path('guardar_equipo/', guardar_equipo, name='guardar_equipo'),
    path('eliminar_equipo/<int:equipo_id>', eliminar_equipo, name='eliminar_equipo'),
    path('editar_equipo/<int:equipo_id>', editar_equipo, name='editar_equipo'),
    path('editar/<int:equipo_id>', editar, name='editar'),
    path('crear_mtto/<int:equipo_id>',crear_mtto, name='crear_mtto'),
    path('guardar_mmto/<int:equipo_id>',guardar_mmto, name='guardar_mmto'),

    

   
]
