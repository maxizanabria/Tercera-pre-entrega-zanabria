from miApp import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from miApp.views import CustomLoginView  

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('consultas/', views.consultas, name='consultas'),
    path('estudios/', views.estudios, name='estudios'),
    path('pacientes-Formulario/', views.pacientes_Formulario, name='pacientesFormulario'),
    path('pacientes-Form-2/', views.pacientes_Form_2, name='pacientesForm2'),
    path('busquedaPacientes/', views.busquedaPacientes, name='BusquedaPacientes'),
    path('buscar/', views.buscar), 
    path('leerPacientes/', views.leerPacientes, name='leerPacientes'), 
    path('eliminarPacientes/<pacientes_nombre>/', views.eliminarPacientes, name="EliminarPacientes"),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
]
