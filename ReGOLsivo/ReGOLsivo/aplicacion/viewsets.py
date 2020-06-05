from rest_framework import viewsets

from .models import Usuario, Administrador, Partido, Pronostico, Comentario, Configuracion, Logro
from .serializer import *
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    """permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAuthenticated],
                                    'edit': [IsAuthenticated],
                                    'delete': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        return super(UsuarioViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(UsuarioViewSet, self).list(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        return super(UsuarioViewSet, self).edit(request, *args, **kwargs)  

    def delete(self, request, *args, **kwargs):
        return super(UsuarioViewSet, self).delete(request, *args, **kwargs)      

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]"""

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

    """permission_classes_by_action = {'create': [IsAdminUser],
                                    'list': [IsAdminUser],
                                    'edit': [IsAdminUser],
                                    'delete': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        return super(AdministradorViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(AdministradorViewSet, self).list(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        return super(AdministradorViewSet, self).edit(request, *args, **kwargs)  

    def delete(self, request, *args, **kwargs):
        return super(AdministradorViewSet, self).delete(request, *args, **kwargs)      

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]"""

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

    """permission_classes_by_action = {'create': [IsAdminUser],
                                    'list': [AllowAny],
                                    'edit': [IsAdminUser],
                                    'delete': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        return super(PartidoViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PartidoViewSet, self).list(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        return super(PartidoViewSet, self).edit(request, *args, **kwargs)  

    def delete(self, request, *args, **kwargs):
        return super(PartidoViewSet, self).delete(request, *args, **kwargs)      

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]"""

class PronosticoViewSet(viewsets.ModelViewSet):
    queryset = Pronostico.objects.all()
    serializer_class = PronosticoSerializer

    """permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [IsAuthenticated],
                                    'edit': [IsAuthenticated],
                                    'delete': [IsAuthenticated]}

    def create(self, request, *args, **kwargs):
        return super(PronosticoViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PronosticoViewSet, self).list(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        return super(PronosticoViewSet, self).edit(request, *args, **kwargs)  

    def delete(self, request, *args, **kwargs):
        return super(PronosticoViewSet, self).delete(request, *args, **kwargs)      

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]"""

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    """permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [IsAuthenticated],
                                    'edit': [IsAuthenticated],
                                    'delete': [IsAuthenticated]}

    def create(self, request, *args, **kwargs):
        return super(ComentarioViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(ComentarioViewSet, self).list(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        return super(ComentarioViewSet, self).edit(request, *args, **kwargs)  

    def delete(self, request, *args, **kwargs):
        return super(ComentarioViewSet, self).delete(request, *args, **kwargs)      

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]"""

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

    """permission_classes_by_action = {'edit': [IsAdminUser]}

    def edit(self, request, *args, **kwargs):
        return super(ConfiguracionViewSet, self).edit(request, *args, **kwargs)      

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]"""

class LogroViewSet(viewsets.ModelViewSet):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer

    """permission_classes_by_action = {'list': [IsAuthenticated],
                                    'edit': [IsAdminUser]}

    def list(self, request, *args, **kwargs):
        return super(LogroViewSet, self).list(request, *args, **kwargs)

    def edit(self, request, *args, **kwargs):
        return super(LogroViewSet, self).edit(request, *args, **kwargs)      

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]"""            