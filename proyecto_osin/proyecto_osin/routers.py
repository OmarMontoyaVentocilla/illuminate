from rest_framework import routers
from persona.viewsets import PersonaViewSet
from search.viewsets import FacebookViewSet
from search.viewsets import TwitterViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'facebook', FacebookViewSet)
router.register(r'twitter', TwitterViewSet)