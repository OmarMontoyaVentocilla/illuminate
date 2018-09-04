# from django.contrib import admin
from django.urls import path
from .views import create_auto, list_auto, update_auto, delete_auto, getAuto, customSearch, get_details, gettw, gethit, getinsta, getgoogle, getcomercio, createfacebook, createtw, creategit, createasig, creategoogle, getinstadet, createinstagram, gettrending
# from django.contrib.auth.decorators import login_required

urlpatterns = [
         path('', list_auto,name='list_auto'),
         path('getauto',getAuto,name='getauto'),
         path('getdet',get_details,name='getdet'),
         path('gettw',gettw,name='gettw'),
         path('gethit',gethit,name='gethit'),
         path('getinsta',getinsta,name='getinsta'),
         path('getinstadet',getinstadet,name='getinstadet'),
         path('getgoogle',getgoogle,name='getgoogle'),
         path('getcomercio', getcomercio,name='getcomercio'),
         path('gettrending', gettrending,name='gettrending'),
         path('addfacebook', createfacebook,name='addfacebook'),
         path('addtwi', createtw,name='addtwi'),
         path('addgit', creategit,name='addgit'),
         path('addgoogle', creategoogle,name='addgoogle'),
         path('addasignacion', createasig,name='addasignacion'),
         path('addainstagram', createinstagram,name='addainstagram'),
         #path('getlinken',getlinken,name='getlinken'),
         path('customsearch',customSearch,name='customsearch'),
         path('add', create_auto,name='create_auto'),
         path('update/<int:id>/', update_auto,name='update_auto'),
         path('delete/<int:id>/', delete_auto,name='delete_auto'),
]
