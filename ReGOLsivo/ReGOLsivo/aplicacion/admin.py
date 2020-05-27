from django.contrib import admin
from aplicacion.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#admin.site.register(CuentaDeUsuario)
#admin.site.register(Actor)

admin.site.register(Usuario, UserAdmin)
admin.site.register(Administrador, UserAdmin)
admin.site.register(Partido)
admin.site.register(Pronostico)
admin.site.register(Comentario)
admin.site.register(Configuracion)