
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, PerfilForm
from .models import UsuarioExtendido

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UsuarioExtendido.objects.create(user=user, es_docente=form.cleaned_data['es_docente'])
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
            return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    perfil = request.user.usuarioextendido
    return render(request, 'accounts/perfil.html', {'perfil': perfil})

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
