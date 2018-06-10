# from django.contrib import admin
from django.urls import path
from .views import create_auto, list_auto, update_auto, delete_auto, getAuto, customSearch, get_details, gettw, gethit, getinsta, getgoogle
# from django.contrib.auth.decorators import login_required

urlpatterns = [
         path('', list_auto,name='list_auto'),
         path('getauto',getAuto,name='getauto'),
         path('getdet',get_details,name='getdet'),
         path('gettw',gettw,name='gettw'),
         path('gethit',gethit,name='gethit'),
         path('getinsta',getinsta,name='getinsta'),
         path('getgoogle',getgoogle,name='getgoogle'),
        #  path('getlinken',getlinken,name='getlinken'),
         path('customsearch',customSearch,name='customsearch'),
         path('add', create_auto,name='create_auto'),
         path('update/<int:id>/', update_auto,name='update_auto'),
         path('delete/<int:id>/', delete_auto,name='delete_auto'),
]
