# from rest_framework import  serializers
# from search.models import *
# from persona.models import *
# from django.contrib.auth.models import User

# class FacebookSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=Facebook
#         fields = ('nombres','biografia','foto','url' )

# class TwitterSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=Twitter
#         fields = ('url','img_tw','nombre_tw')

# class PersonaSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=Persona
#         fields = ('nombre','apodo')


# # class UsuarioSerializer(serializers.ModelSerializer):
    
# #     class Meta:
# #         model=User
# #         fields = ('username')
        
        

# class PersonRedesSerializer(serializers.ModelSerializer):
#     idfb_id = FacebookSerializer(many=True,read_only=True)
#     idtw_id = TwitterSerializer(many=True,read_only=True)
#     idpersona_id =PersonaSerializer(many=True,read_only=True)
#     # idusuario_id =UsuarioSerializer(many=True)
 
#     class Meta:
#         model=PersonaRedes
#         fields = '__all__'
#         #fields = ('facebookdata','twitterdata','personadata')
    