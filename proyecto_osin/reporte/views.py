from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url="/accounts/login")
def listreport(request):
    return render(request,'xxx.html',{})
    #return render(request,'reporte.html',{})