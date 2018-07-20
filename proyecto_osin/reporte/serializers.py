from rest_framework import  serializers

class MiSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    idfb_id=serializers.IntegerField()
    idtw_id=serializers.IntegerField()
    idusuario_id=serializers.IntegerField()
    idpersona_id=serializers.IntegerField()
    estado=serializers.CharField(max_length=3)
    id=serializers.IntegerField()
    idfb=serializers.CharField(max_length=20)
    nombres=serializers.CharField(max_length=150)
    biografia=serializers.CharField(max_length=150)
    foto=serializers.CharField(max_length=150)
    url=serializers.CharField(max_length=150)
    trabajo=serializers.CharField(max_length=150)
    lugar=serializers.CharField(max_length=150)
    estudio=serializers.CharField(max_length=150)
    estado=serializers.CharField(max_length=3)
    id=serializers.IntegerField()
    inicio_tw=serializers.CharField(max_length=150)
    cant_tw=serializers.CharField(max_length=150)
    url=serializers.CharField(max_length=150)
    img_tw=serializers.CharField(max_length=150)
    nombre_tw=serializers.CharField(max_length=150)
    nombre_cuenta_tw=serializers.CharField(max_length=150)
    pagina_web=serializers.CharField(max_length=150)
    biografia=serializers.CharField(max_length=150)
    seguidores=serializers.CharField(max_length=150)
    siguiendo=serializers.CharField(max_length=150)
    tweets=serializers.CharField(max_length=150)
    ubicacion=serializers.CharField(max_length=150)
    likes=serializers.CharField(max_length=150)
    estado=serializers.CharField(max_length=150)
    id=serializers.IntegerField()
    nombre=serializers.CharField(max_length=150)
    apodo=serializers.CharField(max_length=150)
    tiempo_registro=serializers.CharField(max_length=150)
    estado=serializers.CharField(max_length=3)