# from rest_framework import  viewsets
# from rest_framework import  serializers
# from rest_framework.response import Response
# from .serializers import PersonRedesSerializer
# from search.models import *
# from django.contrib.sessions.models import Session
# from rest_framework.views import APIView

# class PersonaRedesViewSet(viewsets.ViewSet):
#     def list(self, format=None):
#         persons=PersonaRedes.objects.all()
#         serializer  = PersonRedesSerializer(persons,many=True)
#         return Response(serializer.data)
        
       
    
    # def list(self, request):
        
        
        #Wreturn Response(serializer.data)
    
    
    #list(self, request):
        
        #return Response(serializer.data)
        
    
    
    

# class MiVistaSet(viewsets.ViewSet):
    
    
    # def list(self, request):
        
    #     yourdata=PersonaRedes.objects.select_related('idfb','idtw','idpersona').filter(idusuario_id=request.session["id_user"])
    #     serializer = MiSerializer(yourdata, many=True)
    #     return Response(serializer.data)