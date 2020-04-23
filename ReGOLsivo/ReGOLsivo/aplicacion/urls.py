from rest_framework import routers

from.viewsets import *

router = routers.SimpleRouter()
router.register('CuentasDeUsuario', CuentaDeUsuarioViewSet)

"""router = routers.SimpleRouter()
router.register('Actores', ActorViewSet)"""

router = routers.SimpleRouter()
router.register('Usuarios', UsuarioViewSet)

router = routers.SimpleRouter()
router.register('Administradores', AdministradorViewSet)

router = routers.SimpleRouter()
router.register('Partidos', PartidoViewSet)

router = routers.SimpleRouter()
router.register('Pronosticos', PronosticoViewSet)

router = routers.SimpleRouter()
router.register('Comentarios', ComentarioViewSet)

router = routers.SimpleRouter()
router.register('Configuraciones', ConfiguracionViewSet)

urlpatterns = router.urls