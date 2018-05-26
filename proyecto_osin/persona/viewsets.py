from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.filter(estado="1")
    serializer_class = PersonaSerializer