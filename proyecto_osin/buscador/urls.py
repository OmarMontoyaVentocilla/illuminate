from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include

from .views import list_people, wseervice



urlpatterns = [
    path('', list_people, name='listpeople'),
    path('wservis', wseervice, name='wservis'),
    # path('<int:question_id>/', views.detail, name='detail'),
]