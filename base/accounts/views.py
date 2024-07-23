from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from .forms import MiFormularioReg, EditarPerfil, MiFormularioCambiarPass
from .models import DatoExtra

def login(request):
    formulario_log = AuthenticationForm()
    
    if request.method == 'POST':
        formulario_log = AuthenticationForm(request, data=request.POST)
        if formulario_log.is_valid():
            usuario = formulario_log.cleaned_data.get('username')
            contrasenia = formulario_log.cleaned_data.get('password')
            
            user = authenticate(request, username=usuario, password=contrasenia)
            
            if user is not None:
                django_login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario no existe. Por favor, regístrese.')
    
    return render(request, 'accounts/login.html', {'formulario_log':formulario_log})


def registro(request):
    
    formulario_reg = MiFormularioReg()
    
    if request.method == "POST":
        formulario_reg = MiFormularioReg(request.POST)
        if formulario_reg.is_valid():
            formulario_reg.save()
            return redirect('login')
    
    return render(request, 'accounts/sign_up.html', {'formulario_reg':formulario_reg})

def ver_perfil(request):
    return render(request, 'accounts/ver_perfil.html')


def editar_perfil(request):
    try:
        datoextra = request.user.datoextra
    except DatoExtra.DoesNotExist:
        datoextra = DatoExtra(user=request.user)
    
    if request.method == "POST":
        formulario_edit = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario_edit.is_valid():
            formulario_edit.save()
            
            if 'avatar' in request.FILES:
                datoextra.avatar = request.FILES['avatar']
                datoextra.save()
            return redirect('ver_perfil')
    else:
        formulario_edit = EditarPerfil(instance=request.user)
    
    return render(request, 'accounts/editar_perfil.html', {'formulario_edit': formulario_edit})


class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    form_class = MiFormularioCambiarPass
    success_url = reverse_lazy('login')
    template_name = 'accounts/cambiar_contra.html'