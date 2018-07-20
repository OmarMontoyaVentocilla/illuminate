from rest_framework import  viewsets
from rest_framework import  serializers
from rest_framework.response import Response
from .serializers import MiSerializer
from search.models import *
from django.contrib.sessions.models import Session

class MiVistaSet(viewsets.ViewSet):
    
    
    def list(self, request):
        
        yourdata=PersonaRedes.objects.select_related('idfb','idtw','idpersona').filter(idusuario_id=request.session["id_user"])
        serializer = MiSerializer(yourdata, many=True)
        return Response(serializer.data)