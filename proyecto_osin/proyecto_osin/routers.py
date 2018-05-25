from rest_framework import routers
from persona.viewsets import PersonaViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)