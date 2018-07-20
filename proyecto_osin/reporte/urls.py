from django.urls import path
from .views import listreport

urlpatterns = [
         path('', listreport,name='listreport'), 
]