from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import datosUsuario, tareasSistem
import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usrObj = authenticate(request, username=nombreUsuario, password=contraUsuario)
        if usrObj is not None:
            login(request,usrObj)
            return HttpResponseRedirect(reverse('app4:perfilUsuario'))
        else:
            return HttpResponseRedirect(reverse('app4:index'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='/')
def perfilUsuario(request):
    if request.method == 'POST':
        nombreTarea = request.POST.get('nombreTarea')
        responsableTarea = request.POST.get('responsableTarea')
        fechaInicio = request.POST.get('fechaInicio')
        fechaFin = request.POST.get('fechaFin')
        descripcionTarea = request.POST.get('descripcionTarea')
        print(nombreTarea)
        print(responsableTarea)
        print(fechaInicio)
        print(fechaFin)
        print(descripcionTarea)
        usrExt = datosUsuario.objects.get(id=responsableTarea)
        tareasSistem.objects.create(
            nombreTarea=nombreTarea,
            descripcionTarea=descripcionTarea,
            fechaFin=datetime.datetime.strptime(fechaFin,'%Y-%m-%d'),
            fechaInicio=datetime.datetime.strptime(fechaInicio,'%Y-%m-%d'),
            estadoTarea='PROGRESO',
            usuarioResponsable=usrExt,
            usuarioCreador=request.user
        )
        return HttpResponseRedirect(reverse('app4:perfilUsuario'))
    return render(request,'informacionUsuario.html',{
        'usuariosExtendidos':datosUsuario.objects.all(),
        'tareasTotales':tareasSistem.objects.all()
    })

@login_required(login_url='/')
def consolaAdministrador(request):
    if request.method == 'POST':
        usernameUsuario = request.POST.get('usernameUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        profesionUsuario = request.POST.get('profesionUsuario')
        emailUsuario = request.POST.get('emailUsuario')
        nroCelular = request.POST.get('nroCelular')
        perfilUsuario = request.POST.get('perfilUsuario')
        usuarioNuevo = User.objects.create(
            username=usernameUsuario,
            email=emailUsuario
        )
        usuarioNuevo.set_password(contraUsuario)
        usuarioNuevo.first_name = nombreUsuario
        usuarioNuevo.last_name = apellidoUsuario
        usuarioNuevo.is_staff = True
        usuarioNuevo.save()
        datosUsuario.objects.create(
            userRel = usuarioNuevo,
            nroCelular = nroCelular,
            profesionUsuario = profesionUsuario,
            perfilUsuario = perfilUsuario
        )
        return HttpResponseRedirect(reverse('app4:consolaAdministrador'))
    return render(request,'consolaAdministrador.html',{
        'usuariosTotales':User.objects.all()
    })

def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('app4:index'))

def finalizarTarea(request,idTarea):
    tareaObj = tareasSistem.objects.get(id=idTarea)
    tareaObj.estadoTarea = 'FINALIZADO'
    tareaObj.save()
    return HttpResponseRedirect(reverse('app4:perfilUsuario'))

def eliminarTarea(request,idTarea):
    tareaObj = tareasSistem.objects.get(id=idTarea)
    tareaObj.delete()
    return HttpResponseRedirect(reverse('app4:perfilUsuario'))

def reanudarTarea(request,idTarea):
    tareaObj = tareasSistem.objects.get(id=idTarea)
    tareaObj.estadoTarea = 'PROGRESO'
    tareaObj.save()
    return HttpResponseRedirect(reverse('app4:perfilUsuario'))
