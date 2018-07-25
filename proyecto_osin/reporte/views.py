from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from search.models import * 
from django.contrib.sessions.models import Session
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.



        
@login_required(login_url="/accounts/login")
def listreport(request):

    obt =PersonaRedes.objects.select_related('idfb','idtw','idpersona').filter(idusuario_id=request.session["id_user"]).all()
    return render(request,'xxx.html',{'obt':obt})

@login_required(login_url="/accounts/login")
def deletereporte(request, id):
    reporte=PersonaRedes.objects.get(id=id)
    reporte.estado='0'
    reporte.save()
    mensaje={}
    mensaje['message']="Se elimno exitosamente"
    return JsonResponse(mensaje)

@login_required(login_url="/accounts/login")
def consultall(request):
    id_persona=request.GET.get('id_persona')
    queryset = list(PersonaRedes.objects.prefetch_related('idfb','idtw','idpersona').filter(idusuario_id=request.session["id_user"],idpersona_id=id_persona,estado=1).all())
    lista = []
    for row in queryset:
        result={}
        result['id']=row.id
        result['nombres_fb']=row.idfb.nombres
        result['biografia_fb']=row.idfb.biografia
        result['foto_fb']=row.idfb.foto
        result['url_fb']=row.idfb.url
        result['trabajo_fb']=row.idfb.trabajo
        result['lugar_fb']=row.idfb.lugar
        result['estudio_fb']=row.idfb.estudio
        result['estado_fb']=row.idfb.estado
        result['inicio_tw']=row.idtw.inicio_tw
        result['cant_tw']=row.idtw.cant_tw
        result['url_tw']=row.idtw.url
        result['img_tw']=row.idtw.img_tw
        result['nombre_tw']=row.idtw.nombre_tw
        result['nombre_cuenta_tw']=row.idtw.nombre_cuenta_tw.strip()
        result['pagina_web_tw']=row.idtw.pagina_web
        result['biografia_tw']=row.idtw.biografia
        result['seguidores_tw']=row.idtw.seguidores
        result['siguiendo_tw']=row.idtw.siguiendo
        result['tweets_tw']=row.idtw.tweets
        result['ubicacion_tw']=row.idtw.ubicacion
        result['likes_tw']=row.idtw.likes
        result['estado_tw']=row.idtw.estado
        result['nombre_persona']=row.idpersona.nombre
        result['apodo_persona']=row.idpersona.apodo
        result['tregistro_persona']=row.idpersona.tiempo_registro
        result['estado_persona']=row.idpersona.estado
        lista.append(result)
        
    data={
        'info':lista
    }    
    return JsonResponse(data)
    #data = serializers.serialize('json', [x.idfb for x in queryset])
    #return HttpResponse(data, content_type='application/json')
    
