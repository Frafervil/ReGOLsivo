from rest_framework import routers

from.viewsets import *

router = routers.SimpleRouter()
router.register('usuarios', UsuarioViewSet)
router.register('administradores', AdministradorViewSet)
router.register('partidos', PartidoViewSet)
router.register('pronosticos', PronosticoViewSet)
router.register('comentarios', ComentarioViewSet)
router.register('configuraciones', ConfiguracionViewSet)
router.register('logros', LogroViewSet)

urlpatterns = router.urls