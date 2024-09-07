from django.contrib import admin
from .models import Pacientes, Registro, Estudios, Consultas

admin.site.register(Pacientes)
admin.site.register(Registro)
admin.site.register(Estudios)
admin.site.register(Consultas)