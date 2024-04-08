from django.db import models
from datetime import date
from django.contrib.auth.models import User

#En esta parte extiende el modelo de usuario predeterminado (User) 
#proporcionado por Django con campos adicionales, como numero de celular, 
#profesion, perfil de usuario y fecha de creación. Esto permite almacenar 
#información adicional relacionada con cada usuario en la base de datos.
class datosUsuario(models.Model):
    userRel = models.OneToOneField(User,on_delete=models.CASCADE)
    nroCelular = models.CharField(max_length=16, null=True, blank=True)
    profesionUsuario = models.CharField(max_length=64, null=True, blank=True)
    perfilUsuario = models.CharField(max_length=512, null=True, blank=True)
    fechaCreacion = models.DateField(default=date.today)

#Ademas, en esta seccion del codigo representa las tareas en un sistema de gestión. 
#Contiene campos para el nombre de la tarea, descripcion, fechas de inicio y finalización, estado de la tarea, y los 
#usuarios creador y responsable. Esto permite organizar y gestionar las tareas asignadas en el sistema.
class tareasSistem(models.Model):
    nombreTarea = models.CharField(max_length=32, null=True, blank=True)
    descripcionTarea = models.CharField(max_length=512, null=True, blank=True)
    fechaFin = models.DateField(default=date.today)
    fechaInicio = models.DateField(default=date.today)
    estadoTarea = models.CharField(max_length=16, null=True, blank=True)
    usuarioCreador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    usuarioResponsable = models.ForeignKey(datosUsuario, on_delete=models.SET_NULL, null=True, blank=True)