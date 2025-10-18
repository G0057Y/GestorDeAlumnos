
from django.db import models
from django.contrib.auth.models import User
from AppGestor.models import Alumno

class UsuarioExtendido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_docente = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(blank=True)
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({'Docente' if self.es_docente else 'Alumno'})"
