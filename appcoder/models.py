from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return (f"Curso: {self.nombre}, Camada: {self.camada}")

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length= 20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    materia = models.CharField(max_length=20)

    def __str__(self):
        return(f"Nombre: {self.nombre}, Apellido: {self.apellido}")

class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
