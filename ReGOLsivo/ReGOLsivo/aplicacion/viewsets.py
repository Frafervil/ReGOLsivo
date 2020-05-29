from rest_framework import viewsets

from .models import Usuario, Administrador, Partido, Pronostico, Comentario, Configuracion
from .serializer import *
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [AllowAny],
                                    'edit': [IsAuthenticated]}

    def create(self, request, *args, **kwargs):
        return super(UsuarioViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(UsuarioViewSet, self).list(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        return super(UsuarioViewSet, self).edit(request, *args, **kwargs)    

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer


class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer


class PronosticoViewSet(viewsets.ModelViewSet):
    queryset = Pronostico.objects.all()
    serializer_class = PronosticoSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer