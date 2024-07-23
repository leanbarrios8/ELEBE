from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Estudios
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class EstudiosListView(ListView):
    model = Estudios
    template_name = 'about/about.html'
    context_object_name = 'estudios'

class AgregarEstudio(LoginRequiredMixin, CreateView):
    model = Estudios
    template_name = 'about/agregar_estudios.html'
    success_url = reverse_lazy('about')
    fields = ['lenguaje', 'duracion', 'nota']
    
class EditarEstudio(LoginRequiredMixin, UpdateView):
    model = Estudios
    template_name = 'about/editar_estudios.html'
    success_url = reverse_lazy('about')
    fields = ['lenguaje', 'duracion', 'nota']
    
class VerEstudio(DetailView):
    model = Estudios
    template_name = 'about/ver_estudios.html'
    
class EliminarEstudio(LoginRequiredMixin, DeleteView):
    model = Estudios
    template_name = 'about/eliminar_estudios.html'
    success_url = reverse_lazy('about')