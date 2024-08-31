from django.db import models

class Pacientes(models.Model): 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField()
    contrasena = models.CharField(max_length=30)
    
class Consultas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    asunto = models.CharField(max_length=20)
    detalle = models.CharField(max_length=300)

class Estudios(models.Model):
    nombre = models.CharField(max_length=30)   
    fecha_de_entrega = models.DateField(default=False)
    entregado = models.BooleanField(default=False)       