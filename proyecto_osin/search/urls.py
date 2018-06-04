# from django.contrib import admin
from django.urls import path
from .views import create_auto, list_auto, update_auto, delete_auto, getAuto, customSearch, get_details, gettw, gettwts
# from django.contrib.auth.decorators import login_required

urlpatterns = [
         path('', list_auto,name='list_auto'),
         path('getauto',getAuto,name='getauto'),
         path('getdet',get_details,name='getdet'),
         path('gettw',gettw,name='gettw'),
         path('gettwts',gettwts,name='gettwts'),
         path('customsearch',customSearch,name='customsearch'),
         path('add', create_auto,name='create_auto'),
         path('update/<int:id>/', update_auto,name='update_auto'),
         path('delete/<int:id>/', delete_auto,name='delete_auto'),
]
