"""
URL configuration for vehiculos_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from vehiculos.views import *
from django.http import HttpResponse

router = DefaultRouter()
router.register('marcas', MarcaViewSet)
router.register('modelos', ModeloViewSet)
router.register('versiones', VersionViewSet)
router.register('vehiculos', VehiculoViewSet)
router.register('clientes', ClienteViewSet)
router.register('vendedores', VendedorViewSet)
router.register('paises', PaisViewSet)
router.register('ventas', VentaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', lambda request: HttpResponse("Hola"), name='home'),
    path('api/', include(router.urls)),
]