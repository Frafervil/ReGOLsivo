from rest_framework import routers

from.viewsets import UsuarioViewSet

router = routers.SimpleRouter()
router.register('usuarios', UsuarioViewSet)

urlpatterns = router.urls