from django.urls import path
from .views import listreport, consultall

urlpatterns = [
         path('', listreport,name='listreport'),
         path('consultall', consultall,name='consultall'), 
]