#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from persona.models import *

# Create your models here.
class Auto(models.Model):
    placa=models.CharField(max_length=8,unique=True)
    nombres=models.CharField(max_length=100)
    email=models.EmailField(blank=False)
    descripcion_vida=models.TextField()
    edad=models.IntegerField()
    tiempo_registro=models.DateTimeField(auto_now=True)
    cantidad_dinero=models.DecimalField(max_digits=5,decimal_places=2)
    thumb=models.ImageField(default='default.png',blank=True)


    def __str__(self):
        return self.nombres


class Facebook(models.Model):
    idfb=models.CharField(unique=True,null=True,max_length=17)
    nombres=models.CharField(max_length=100)
    biografia=models.TextField()
    foto=models.TextField()
    url=models.TextField()
    trabajo=models.CharField(max_length=300)
    lugar=models.CharField(max_length=300)
    estudio=models.CharField(max_length=300)
    estado=models.CharField(max_length=2)


class Twitter(models.Model):
    inicio_tw=models.CharField(max_length=100)
    cant_tw=models.CharField(max_length=50)
    url=models.TextField()
    img_tw=models.TextField()
    nombre_tw=models.CharField(max_length=50)
    nombre_cuenta_tw=models.CharField(max_length=150)
    pagina_web=models.TextField()
    biografia=models.TextField()
    seguidores=models.CharField(max_length=50)
    siguiendo=models.CharField(max_length=50)
    tweets=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)
    likes=models.CharField(max_length=50)
    estado=models.CharField(max_length=2)


class Google(models.Model):
    nombre_google=models.CharField(max_length=150)
    url_google=models.TextField()
    img_google=models.TextField()
    info_google=models.TextField()
    estado=models.CharField(max_length=2)
    

class Instagram(models.Model):
    nombre_instagram=models.TextField()
    usuario_instagram=models.CharField(max_length=150)
    url_instagram=models.CharField(max_length=250)
    foto_instagram=models.CharField(max_length=280)
    seguidores_instagram=models.CharField(max_length=150)
    post_instagram=models.CharField(max_length=150)
    siguiendo_instagram=models.CharField(max_length=150)
    estado=models.CharField(max_length=2)

class Github(models.Model):
    biografia_github=models.TextField()
    email_github=models.CharField(max_length=100)
    img_github=models.CharField(max_length=250)
    nick_github=models.CharField(max_length=100)
    nombre_github=models.CharField(max_length=150)
    pagina_github=models.TextField()
    pais_github=models.CharField(max_length=100)
    estado=models.CharField(max_length=2)


class PersonaRedes(models.Model):
    idfb=models.ForeignKey(Facebook,related_name='facebookdata',on_delete=models.CASCADE,blank=True, null=True)
    idtw=models.ForeignKey(Twitter,related_name='twitterdata',on_delete=models.CASCADE,blank=True, null=True)
    idgoogle=models.ForeignKey(Google,related_name='googledata',on_delete=models.CASCADE,blank=True, null=True) 
    idinstagram=models.ForeignKey(Instagram,related_name='instagramdata',on_delete=models.CASCADE,blank=True, null=True)
    idgithub=models.ForeignKey(Github,related_name='githubdata',on_delete=models.CASCADE,blank=True, null=True)   
    idusuario=models.ForeignKey(User,related_name='usuariodata',on_delete=models.CASCADE,blank=True, null=True)
    idpersona=models.ForeignKey(Persona,related_name='personadata',on_delete=models.CASCADE)
    estado=models.CharField(max_length=2)





