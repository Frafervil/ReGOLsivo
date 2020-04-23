from django.contrib import admin
from aplicacion.models import *
# Register your models here.

admin.site.register(CuentaDeUsuario)
#admin.site.register(Actor)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Partido)
admin.site.register(Pronostico)
admin.site.register(Comentario)
admin.site.register(Configuracion)