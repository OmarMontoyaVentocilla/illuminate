from django.urls import path
from .views import createpersona, listpersona, deletepersona, editpersona

urlpatterns = [
         path('', listpersona,name='listpersona'), 
         path('addpersona', createpersona,name='addpersona'),
         path('deletepersona/<int:id>/', deletepersona,name='deletepersona'),
         path('editpersona/<int:id>/', editpersona,name='editpersona') 
        #  path('get',getAuto,name='getauto'),
        #  path('getdet',get_details,name='getdet'),
        #  #  path('gettw',gettw,name='gettw'),
        #  path('customsearch',customSearch,name='customsearch'),
        #  path('add', create_auto,name='create_auto'),
        #  path('update/<int:id>/', update_auto,name='update_auto'),
        #  path('delete/<int:id>/', delete_auto,name='delete_auto'),
]