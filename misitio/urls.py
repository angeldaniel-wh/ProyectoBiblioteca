"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from misitio import settings
from django.conf.urls.static import static

from misitio.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hola/$', hola),
    url(r'^fecha_actual/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante),
    url(r'^encabezados/$', encabezados_http, name='encabezados'),
    url(r'^formulario-buscar/$', formulario_buscar),
    url(r'^buscar/$', buscar),
    url(r'^contactos/$', contactos),
    url(r'^contactos/gracias/$', contactos_gracias),
    url(r'^biblioteca/', include('apps.biblioteca.urls', namespace='biblioteca')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)