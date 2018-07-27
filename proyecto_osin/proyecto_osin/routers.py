from rest_framework import routers
from persona.viewsets import PersonaViewSet
from search.viewsets import FacebookViewSet
from search.viewsets import TwitterViewSet
from search.viewsets import GoogleViewSet
# from reporte.viewsets import PersonaRedesViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'facebook', FacebookViewSet)
router.register(r'twitter', TwitterViewSet)
router.register(r'google', GoogleViewSet)
# router.register(r'listadotodo',PersonaRedesViewSet,base_name='listado') 