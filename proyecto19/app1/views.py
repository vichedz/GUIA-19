from django.shortcuts import render, redirect
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from .formularios.proveedorform import ProveedorForm
from .formularios.productosform import ProductoForm
from django.http import HttpResponseRedirect
from .models import Productos, Proveedores
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
    return render(request, "Reg_user.html", {"form": formulario})


def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user': request.user, 'es_estudiante': es_estudiante, 'es_admin': es_admin})
    else:
        return render(request, 'index.html', {'user': request.user, 'es_estudiante': es_estudiante, 'es_admin': es_admin})


def agregar_proveedor(request):
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('proveedores')
    else:
        formulario = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': formulario})


def proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})


def agregar_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos')
    else:
        formulario = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': formulario})


def productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = LoginForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(
                    request, "Usuario o contraseña incorrectos. Intente de nuevo.")
    else:
        formulario = LoginForm()
    return render(request, 'login.html', {'form': formulario})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    return render(request, 'index.html', {'user': request.user, 'es_estudiante': es_estudiante, 'es_admin': es_admin})
