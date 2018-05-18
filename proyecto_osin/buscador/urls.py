from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include

from .views import list_people

urlpatterns = [
    path('', list_people, name='listpeople'),
    # path('<int:question_id>/', views.detail, name='detail'),
]