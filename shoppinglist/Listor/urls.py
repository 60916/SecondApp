from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AllaListor.as_view(), name='lista-hem'),
    path('lista/<int:pk>', views.EnLista.as_view(), name='lista-sida'),
    path('lista/ny', views.NyLista.as_view(), name='lista-ny'),
]
