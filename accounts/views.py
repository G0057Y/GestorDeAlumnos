
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, PerfilForm
from .models import UsuarioExtendido
from AppGestor.models import Alumno, Asistencia, TrabajoPractico

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            usuario_ext = UsuarioExtendido.objects.create(user=user, es_docente=form.cleaned_data['es_docente'])
            
            # Si no es docente, crear también el Alumno, porque son 2 entidades separadas
            # Sin esto me creaba un usuario genérico que no tenia un alumno asociado.
            if not usuario_ext.es_docente:
                alumno = Alumno.objects.create(
                    nombre=user.first_name or user.username,
                    apellido=user.last_name or "",
                    email=user.email,
                    curso="Sin curso",
                    fecha_ingreso="1900-01-01"
                )
                usuario_ext.alumno = alumno
                usuario_ext.save()
            
            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redireccion_por_rol(request)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    perfil = request.user.usuarioextendido
    #para que muestre el dato de asistencias y trabajos entregados en el perfil de usuario
    usuario = request.user
    try:
        alumno = Alumno.objects.get(email=usuario.email)
        asistencias = Asistencia.objects.filter(alumno=alumno)
        trabajos = TrabajoPractico.objects.filter(alumno=alumno)
    except Alumno.DoesNotExist:
        asistencias = []
        trabajos = []


    return render(request, 'accounts/perfil.html', {'perfil': perfil, 
    #'form': form,
    'asistencias': asistencias,
    'trabajos': trabajos})

@login_required
def editar_perfil(request):
    perfil = request.user.usuarioextendido
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'accounts/editar_perfil.html', {'form': form})


def redireccion_por_rol(request):
    if request.user.usuarioextendido.es_docente:
        return redirect('alumno_list')
    else:
        return redirect('perfil')
