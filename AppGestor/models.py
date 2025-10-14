from django.db import models

from ckeditor.fields import RichTextField  

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=50)
    biografia = RichTextField(default="Sin biografía")
    foto = models.ImageField(upload_to='alumnos/', null=True, blank=True)
    fecha_ingreso = models.DateField(default="1900-01-01")


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
