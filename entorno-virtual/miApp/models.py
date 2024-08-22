from django.db import models

class Pacientes(models.Model): 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Consultas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class estudios(models.Model):
    nombre = models.CharField(max_length=30)   
    fecha_de_entrega = models.DateField(default=False)
    entregado = models.BooleanField(default=False)       