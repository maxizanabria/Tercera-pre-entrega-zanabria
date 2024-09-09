from django.db import models

class Pacientes(models.Model): 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"
    
    

class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    contrasena = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Contrasena: {self.contrasena} - Edad: {self.edad}"
    
class Consultas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    asunto = models.CharField(max_length=20)
    detalle = models.CharField(max_length=300)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.detalle} - Asunto : {self.asunto}"

class Estudios(models.Model):
    nombre = models.CharField(max_length=30)   
    fecha_de_entrega = models.DateField(default=False)
    reservado = models.BooleanField(default=False)       
    
    
    def __str__(self):
        texto_reservado = "Reservado" if self.reservado else "No entregado"
        return f"Reservado para: {self.nombre} | Fecha: {self.fecha_de_entrega} | Estado: {texto_reservado}"