from rest_framework import routers
from persona.viewsets import PersonaViewSet
from search.viewsets import FacebookViewSet
from search.viewsets import TwitterViewSet
from reporte.viewsets import MiVistaSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'facebook', FacebookViewSet)
router.register(r'twitter', TwitterViewSet)
router.register(r'listadotodo',MiVistaSet,base_name='listado')