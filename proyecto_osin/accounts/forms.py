from django.contrib.auth.forms import AuthenticationForm 
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'type':'text','class': 'form-control', 'name': 'username','autocomplete':'off'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'type':'password','class': 'form-control', 'name': 'password'}))