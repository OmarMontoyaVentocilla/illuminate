from django.urls import path
from .views import listreport, consultall, deletereporte 

urlpatterns = [
         path('', listreport,name='listreport'),
         path('deletereporte/<int:id>/', deletereporte,name='deletereporte'),
         path('consultall', consultall,name='consultall'), 
]