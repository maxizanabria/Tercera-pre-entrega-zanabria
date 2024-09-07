from miApp import views 
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio,name='inicio'),
    path('pacientes/', views.pacientes,name='pacientes'),
    path('consultas/', views.consultas,name='consultas'),
    path('estudios/', views.estudios,name='estudios'),
    path('pacientes-Formulario/', views.pacientes_Formulario,name='pacientesFormulario'),
    path('pacientes-Form-2/', views.pacientes_Form_2, name='pacientesForm2'),
    path('busquedaPacientes/', views.busquedaPacientes, name='BusquedaPacientes'),
    path('buscar/', views.buscar), 
    
]
