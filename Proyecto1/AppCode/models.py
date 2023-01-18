from django.db import models

# Create your models here.

class Odontologo(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=  models.CharField(max_length=50)
    numero_matricula= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Numero Matricula: {self.numero_matricula}"

class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    edad= models.IntegerField()
    email= models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Edad: {self.edad} - Email: {self.email}"

class Turno(models.Model):
    fecha= models.DateField()
    dni_paciente= models.IntegerField()
    apellido_doctor= models.CharField(max_length=50)
