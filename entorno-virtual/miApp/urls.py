from miApp import views 
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio),
    path('pacientes/', views.pacientes),
    path('consultas/', views.consultas),
    path('estudios/', views.estudios),
]
