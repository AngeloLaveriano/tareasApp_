from django.apps import AppConfig

#Aqui se establece el campo automático predeterminado para la base de datos y se asigna el 
#nombre de la aplicación. Esto ayuda a Django a gestionar la aplicación correctamente
class App4Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app4'
