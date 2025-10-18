from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import UsuarioExtendido
from AppGestor.models import Alumno
#Este archivo es para poder unir el Alumno creado con form con el usuario correspondiente
#Porque si no, quedaban disociados y el alumno no podia ver su asistencia.

#UPDATE: no terminé de hacerlo funcionar y desistí por ahora. lo dejo para completarlo en el futuro

@receiver(post_save, sender=Alumno)
def crear_usuario_para_alumno(sender, instance, created, **kwargs):
    if created:
        username = f"{instance.nombre.lower()}.{instance.apellido.lower()}"
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=instance.email,
                password="1234"
            )
            UsuarioExtendido.objects.create(
                user=user,
                es_docente=False,
                alumno=instance
            )