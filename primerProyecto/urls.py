"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

#Cada ruta especifica un prefijo de URL (admin/, app2/, app3/, app1/) seguido de las URL 
#definidas en las respectivas aplicaciones (app4.urls, app2.urls, app3.urls, app1.urls). 
#Esto permite acceder a las vistas y funcionalidades de cada aplicación mediante rutas específicas.
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('app4.urls')),
    #En esta parte se configura que cada vez que se acceda al sitio wweb,
    #sin ninguna division, se acceda a app4

    path('app2/',include('app2.urls')),
    path('app3/',include('app3.urls')),
    path('app1/',include('app1.urls')),
]