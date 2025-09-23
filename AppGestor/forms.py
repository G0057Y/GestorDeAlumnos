from django import forms
from .models import Alumno

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    curso = forms.CharField(max_length=50)

class AsistenciaFormulario(forms.Form):
    alumno = forms.ModelChoiceField(
        queryset=Alumno.objects.all(),
        label="Alumno"
    )
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    presente = forms.BooleanField(required=False)
'''
class TrabajoPracticoFormulario(forms.Form):
    alumno_id = forms.IntegerField(label="ID del alumno")
    titulo = forms.CharField(max_length=100)
    entregado = forms.BooleanField(required=False)
    fecha_entrega = forms.DateField()
'''

class TrabajoPracticoFormulario(forms.Form):
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.all())
    titulo = forms.CharField(max_length=100)
    entregado = forms.BooleanField(required=False)
    fecha_entrega = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class BuscarAlumnoFormulario(forms.Form):
    apellido = forms.CharField(max_length=100)
