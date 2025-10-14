from django.shortcuts import render
from .forms import AlumnoFormulario, AsistenciaFormulario, TrabajoPracticoFormulario, BuscarAlumnoFormulario
from .models import Alumno, Asistencia, TrabajoPractico

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def inicio(request):
    return render(request, "AppGestor/inicio.html")

def alumnoFormulario(request):
    if request.method == "POST":
        form = AlumnoFormulario(request.POST)
        if form.is_valid():
            Alumno.objects.create(**form.cleaned_data)
            return render(request, "AppGestor/exito.html")
    else:
        form = AlumnoFormulario()
    return render(request, "AppGestor/formulario.html", {"form": form, "titulo": "Agregar Alumno"})
'''
def asistenciaFormulario(request):
    if request.method == "POST":
        form = AsistenciaFormulario(request.POST)
        if form.is_valid():
            alumno = Alumno.objects.get(id=form.cleaned_data["alumno_id"])
            Asistencia.objects.create(alumno=alumno, fecha=form.cleaned_data["fecha"], presente=form.cleaned_data["presente"])
            return render(request, "AppGestor/exito.html")
    else:
        form = AsistenciaFormulario()
    return render(request, "AppGestor/formulario.html", {"form": form, "titulo": "Registrar Asistencia"})
'''
@login_required
def asistenciaFormulario(request):
    #Solo lo muestro a los docentes
    if not request.user.usuarioextendido.es_docente:
        return HttpResponseForbidden("Solo los docentes pueden registrar asistencia.")

    if request.method == "POST":
        form = AsistenciaFormulario(request.POST)
        if form.is_valid():
            Asistencia.objects.create(
                alumno=form.cleaned_data["alumno"],   # 👈 ya es un objeto Alumno
                fecha=form.cleaned_data["fecha"],
                presente=form.cleaned_data["presente"],
            )
            return render(request, "AppGestor/exito.html")
    else:
        form = AsistenciaFormulario()
    return render(request, "AppGestor/formulario.html", {"form": form, "titulo": "Registrar Asistencia"})
""" 
def trabajoFormulario(request):
    if request.method == "POST":
        form = TrabajoPracticoFormulario(request.POST)
        if form.is_valid():
            alumno = Alumno.objects.get(id=form.cleaned_data["alumno_id"])
            TrabajoPractico.objects.create(alumno=alumno, titulo=form.cleaned_data["titulo"], entregado=form.cleaned_data["entregado"], fecha_entrega=form.cleaned_data["fecha_entrega"])
            return render(request, "AppGestor/exito.html")
    else:
        form = TrabajoPracticoFormulario()
    return render(request, "AppGestor/formulario.html", {"form": form, "titulo": "Registrar Trabajo Práctico"})
 """
def trabajoFormulario(request):
    if request.method == "POST":
        form = TrabajoPracticoFormulario(request.POST)
        if form.is_valid():
            trabajo = TrabajoPractico.objects.create(
                alumno=form.cleaned_data["alumno"],
                titulo=form.cleaned_data["titulo"],
                entregado=form.cleaned_data["entregado"],
                fecha_entrega=form.cleaned_data["fecha_entrega"],
            )
            return render(request, "AppGestor/inicio.html", {"mensaje": "Trabajo práctico guardado"})
    else:
        form = TrabajoPracticoFormulario()

    return render(request, "AppGestor/formulario.html", {"form": form, "titulo": "Registrar Trabajo Práctico"})


def buscarAlumno(request):
    resultados = []
    if request.method == "GET":
        form = BuscarAlumnoFormulario(request.GET)
        if form.is_valid():
            apellido = form.cleaned_data["apellido"]
            resultados = Alumno.objects.filter(apellido__icontains=apellido)
    else:
        form = BuscarAlumnoFormulario()
    return render(request, "AppGestor/buscar.html", {"form": form, "resultados": resultados})

### CRUD DE ALUMNO ###

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'AppGestor/alumno_list.html'

class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'AppGestor/alumno_detail.html'

class AlumnoCreateView(LoginRequiredMixin, CreateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email', 'curso', 'biografia', 'foto', 'fecha_ingreso']
    template_name = 'AppGestor/alumno_form.html'
    success_url = '/alumnos/'

class AlumnoUpdateView(LoginRequiredMixin, UpdateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email', 'curso', 'biografia', 'foto', 'fecha_ingreso']
    template_name = 'AppGestor/alumno_form.html'
    success_url = '/alumnos/'

class AlumnoDeleteView(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = 'AppGestor/alumno_confirm_delete.html'
##### 