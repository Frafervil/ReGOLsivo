from rest_framework import viewsets

from .models import Usuario, Administrador, Partido, Pronostico, Comentario, Configuracion, Logro
from .serializer import *
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

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

class LogroViewSet(viewsets.ModelViewSet):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer          