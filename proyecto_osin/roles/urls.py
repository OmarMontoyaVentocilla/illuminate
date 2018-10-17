from django.urls import path
from .views import listroles, adduser


urlpatterns = [
         path('', listroles,name='listroles'),
         path('adduser',adduser,name='adduser'),
]