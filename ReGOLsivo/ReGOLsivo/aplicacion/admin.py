from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from aplicacion.models import *
# Register your models here.  

admin.site.register(User, UserAdmin)

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Partido)
admin.site.register(Pronostico)
admin.site.register(Comentario)
admin.site.register(Configuracion)