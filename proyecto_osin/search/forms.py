from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):
     class Meta:
         model=Auto
         fields=['placa','nombres','email','descripcion_vida','edad','cantidad_dinero']
