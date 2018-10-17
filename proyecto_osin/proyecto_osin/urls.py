"""proyecto_osin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .routers import router
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('asignacion/', include('buscador.urls')),
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('search/',include('search.urls')),
    path('accounts/',include('accounts.urls')),
    path('persona/',include('persona.urls')),
    path('reporte/',include('reporte.urls')),
    path('roles/',include('roles.urls')),
    # TemplateView.as_view(template_name='persona.html')
    #path('persona/',view=TemplateView.as_view(template_name='persona.html')),
    path('api/', include(router.urls))
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



