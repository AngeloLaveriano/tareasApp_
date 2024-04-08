from django.urls import path
from . import views

app_name='app4'

#En esta parte del codigo se encarga de asignar las URLs a las vistas correspondientes en las vistas de la 
#aplicación. Cada ruta define una dirección URL específica , en la app4, que el usuario puede visitar y la función 
#de vista que se ejecutará cuando se acceda a esa URL.
urlpatterns = [
    path('',views.index,name='index'),
    path('perfilUsuario',views.perfilUsuario,name='perfilUsuario'),
    path('consolaAdministrador',views.consolaAdministrador,name='consolaAdministrador'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('finalizarTarea/<str:idTarea>',views.finalizarTarea,name='finalizarTarea'),
    path('eliminarTarea/<str:idTarea>',views.eliminarTarea,name='eliminarTarea'),
    path('reanudarTarea/<str:idTarea>',views.reanudarTarea,name='reanudarTarea'),
]