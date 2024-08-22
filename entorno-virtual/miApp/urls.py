from miApp import views 
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio,name='inicio'),
    path('pacientes/', views.pacientes,name='pacientes'),
    path('consultas/', views.consultas,name='consultas'),
    path('estudios/', views.estudios,name='estudios'),
    path('pacientes-Formulario/', views.pacientes_Formulario,name='pacientesFormulario'),
    
]
