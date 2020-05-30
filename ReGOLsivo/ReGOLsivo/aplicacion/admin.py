from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from aplicacion.models import *
# Register your models here.  

admin.site.register(Usuario, UserAdmin)
admin.site.register(Administrador, UserAdmin)
admin.site.register(Logro)
admin.site.register(Partido)
admin.site.register(Pronostico)
admin.site.register(Comentario)
admin.site.register(Configuracion)