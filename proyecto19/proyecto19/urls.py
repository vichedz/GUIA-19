"""
URL configuration for proyecto19 project.

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
from app1 import views as ap1v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ap1v.index, name="home"),
    path('registro/', ap1v.reg_user, name="registro"),
    path('login/', ap1v.iniciar_sesion, name="login"),
    path('logout/', ap1v.cerrar_sesion, name='logout'),
    path('proveedores/', ap1v.proveedores, name='proveedores'),
    path('agregar_proveedor/', ap1v.agregar_proveedor, name='agregar_proveedor'),
    path('productos/', ap1v.productos, name='productos'),
    path('agregar_producto/', ap1v.agregar_producto, name='agregar_producto'),
]
