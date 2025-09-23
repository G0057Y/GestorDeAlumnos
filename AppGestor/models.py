from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField()

class TrabajoPractico(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    entregado = models.BooleanField()
    fecha_entrega = models.DateField()
