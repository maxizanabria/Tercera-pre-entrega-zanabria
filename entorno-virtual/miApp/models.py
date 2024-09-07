from django.db import models

class Pacientes(models.Model): 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
    

class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    contrasena = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre} - {self.contrasena}"
    
class Consultas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    asunto = models.CharField(max_length=20)
    detalle = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.nombre} - {self.detalle}"

class Estudios(models.Model):
    nombre = models.CharField(max_length=30)   
    fecha_de_entrega = models.DateField(default=False)
    entregado = models.BooleanField(default=False)       
    
    
    def __str__(self):
        texto_entregado = "Entregado" if self.entregado else "No entregado"
        return f"Entregable: {self.nombre} | Fecha: {self.fecha_de_entrega} | Estado: {texto_entregado}"