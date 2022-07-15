"""entrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from mi_app.forms import Cargar_auto
from mi_app.views import buscar_juego, instanciar_familiar, listar_familia, listar_autos, listar_juegos, instanciar_juegos, instanciar_auto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', listar_familia),
    path('juegos/', listar_juegos),
    path('autos/', listar_autos),
    path('cargar-juegos', instanciar_juegos),
    path('cargar-familiar', instanciar_familiar),
    path('cargar-autos', instanciar_auto),
    path('buscar-juegos', buscar_juego),
    
    
]
