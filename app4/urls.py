from django.urls import path
from . import views

app_name='app4'

urlpatterns = [
    path('',views.index,name='index'),
    path('perfilUsuario',views.perfilUsuario,name='perfilUsuario'),
    path('consolaAdministrador',views.consolaAdministrador,name='consolaAdministrador'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('finalizarTarea/<str:idTarea>',views.finalizarTarea,name='finalizarTarea'),
    path('eliminarTarea/<str:idTarea>',views.eliminarTarea,name='eliminarTarea'),
    path('reanudarTarea/<str:idTarea>',views.reanudarTarea,name='reanudarTarea'),
]