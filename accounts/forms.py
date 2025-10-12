
from django import forms
from django.contrib.auth.models import User
from .models import UsuarioExtendido

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    es_docente = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioExtendido
        fields = ['avatar', 'biografia']
