from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import requests
import json
from .models import Persona
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/accounts/login")
def createpersona(request):
    if(request.method == 'POST'):
        valor=json.loads(request.body.decode("utf-8"))
        nombre = valor['nombre'].strip()
        apodo = valor['apodo'].strip()
        mensaje={}
        if(nombre!=''):
            persona=Persona.objects.create(nombre=nombre,apodo=apodo)
            if(persona):
                mensaje['success']="Se guardo exitosamente"
            else:
                mensaje['fail']="No se guardo"
        else:
            mensaje['fail']="No se guardo"                
    return JsonResponse(mensaje)

@login_required(login_url="/accounts/login")      
def deletepersona(request, id):
    persona=Persona.objects.get(id=id)
    delete=persona.delete()
    if(delete):
        mensaje={}
        mensaje['message']="Se elimno exitosamente"
    return JsonResponse(mensaje)

def editpersona(request,id):
    valor="mi id es: {}".format(id)
    # persona=Persona.objects.get(id=id)
    return HttpResponse(valor)


@login_required(login_url="/accounts/login")
def listpersona(request):
    personas=Persona.objects.all()
    return render(request,'persona.html',{'personas':personas})