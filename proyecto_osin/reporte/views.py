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
    queryset = list(PersonaRedes.objects.prefetch_related('idfb','idtw','idgoogle','idinstagram','idgithub','idpersona').filter(idusuario_id=request.session["id_user"],idpersona_id=id_persona,estado=1).all())
    lista = []
    for row in queryset:
        result={}
        result['id']=row.id
        if(row.idfb):
            result['nombres_fb']=row.idfb.nombres
            result['biografia_fb']=row.idfb.biografia
            result['foto_fb']=row.idfb.foto
            result['url_fb']=row.idfb.url
            result['trabajo_fb']=row.idfb.trabajo
            result['lugar_fb']=row.idfb.lugar
            result['estudio_fb']=row.idfb.estudio
            result['estado_fb']=row.idfb.estado
        else:
            result['nombres_fb']="No existe información"
            result['biografia_fb']="No existe información"
            result['foto_fb']=""
            result['url_fb']="No existe información"
            result['trabajo_fb']="No existe información"
            result['lugar_fb']="No existe información"
            result['estudio_fb']="No existe información"
            result['estado_fb']="No existe información"
                
        
        if(row.idtw):
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
        else:
            result['inicio_tw']="No existe información"
            result['cant_tw']="No existe información"
            result['url_tw']="No existe información"
            result['img_tw']=""
            result['nombre_tw']="No existe información"
            result['nombre_cuenta_tw']="No existe información"
            result['pagina_web_tw']="No existe información"
            result['biografia_tw']="No existe información"
            result['seguidores_tw']="No existe información"
            result['siguiendo_tw']="No existe información"
            result['tweets_tw']="No existe información"
            result['ubicacion_tw']="No existe información"
            result['likes_tw']="No existe información"
            result['estado_tw']="No existe información"
            
        
        if(row.idgoogle):
            result['nombre_google']=row.idgoogle.nombre_google
            result['url_google']=row.idgoogle.url_google
            result['img_google']=row.idgoogle.img_google
            result['info_google']=row.idgoogle.info_google
            result['estado_google']=row.idgoogle.estado
        else:
            result['nombre_google']="No existe información"
            result['url_google']="No existe información"
            result['img_google']=""
            result['info_google']="No existe información"
            result['estado_google']="No existe información"
            
        
        if(row.idpersona):
            result['nombre_persona']=row.idpersona.nombre
            result['apodo_persona']=row.idpersona.apodo
            result['tregistro_persona']=row.idpersona.tiempo_registro
            result['estado_persona']=row.idpersona.estado
        
        if(row.idinstagram):
            result['nombre_instagram']=row.idinstagram.nombre_instagram
            result['usuario_instagram']=row.idinstagram.usuario_instagram
            result['url_instagram']=row.idinstagram.url_instagram
            result['foto_instagram']=row.idinstagram.foto_instagram
            result['seguidores_instagram']=row.idinstagram.seguidores_instagram
            result['post_instagram']=row.idinstagram.post_instagram
            result['siguiendo_instagram']=row.idinstagram.siguiendo_instagram
            result['estado_instagram']=row.idinstagram.estado
        else:
            result['nombre_instagram']="No existe información"
            result['usuario_instagram']="No existe información"
            result['url_instagram']="No existe información"
            result['foto_instagram']=""
            result['seguidores_instagram']="No existe información"
            result['post_instagram']="No existe información"
            result['siguiendo_instagram']="No existe información"
            result['estado_instagram']="No existe información"
            
        
        if(row.idgithub):
            result['biografia_github']=row.idgithub.biografia_github
            result['email_github']=row.idgithub.email_github
            result['img_github']=row.idgithub.img_github
            result['nick_github']=row.idgithub.nick_github
            result['nombre_github']=row.idgithub.nombre_github
            result['pagina_github']=row.idgithub.pagina_github
            result['pais_github']=row.idgithub.pais_github
            result['estado_github']=row.idgithub.estado
        else:
            result['biografia_github']="No existe información"
            result['email_github']="No existe información"
            result['img_github']=""
            result['nick_github']="No existe información"
            result['nombre_github']="No existe información"
            result['pagina_github']="No existe información"
            result['pais_github']="No existe información"
            result['estado_github']="No existe información"
             
        
        lista.append(result)
        
    data={
        'info':lista
    }    
    return JsonResponse(data)
    #data = serializers.serialize('json', [x.idfb for x in queryset])
    #return HttpResponse(data, content_type='application/json')
    
