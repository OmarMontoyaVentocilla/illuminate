from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .forms import LoginForm
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
        form=LoginForm(data=request.POST)
        if (form.is_valid()):
            user=form.get_user()
            login(request,user)
            if request.user.is_authenticated:
                request.session["id_user"] = user.id
            return redirect('list_auto')
    else:
        form=LoginForm()
    
    return render(request,'login.html',{'form':form})

def logout_view(request):
    if (request.method=='POST'):
        del request.session['id_user']
        logout(request)
        return redirect('accounts:login')