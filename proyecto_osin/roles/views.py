from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from search.models import * 
from django.contrib.sessions.models import Session
import json
import requests
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User, Permission
from .forms import RegistroForm
# Create your views here.

def listroles(request):
     if (request.method=='POST'):
         form=RegistroForm(request.POST)
         if (form.is_valid()):
             user=form.save()
             return redirect('listroles')
     else:
         form=RegistroForm()

     userlist=User.objects.all() 
     return render(request,'rol.html',{'form':form,'userlist':userlist})


def adduser(request):
    return HttpResponse("1")
