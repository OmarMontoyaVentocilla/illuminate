from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    #return HttpResponse("fdfdf");
    response=requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    myText={
        'data':"PRUEBA DE DATA",
        'ip':geodata['ip'],
        'country': geodata['country_name']
    }
    return render(request,'proyect_osin/index.html',context=myText)

    
