from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def signup(request):
    if (request.method=='POST'):
        form=UserCreationForm(request.POST)
        if (form.is_valid()):
            user=form.save()
            login(request,user)
            return redirect('list_auto')
    else:
        form=UserCreationForm()
        
    return render(request,'index.html',{'form':form})

def login_view(request):
    if (request.method=='POST'):
        form=AuthenticationForm(data=request.POST)
        if (form.is_valid()):
            user=form.get_user()
            login(request,user)
            return redirect('list_auto')
    else:
        form=AuthenticationForm()
    
    return render(request,'login.html',{'form':form})

def logout_view(request):
    if (request.method=='POST'):
        logout(request)
        return redirect('list_auto')