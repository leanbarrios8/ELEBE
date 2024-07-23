from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Monedas
from .forms import BusquedaMonedas
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class MonedaListView(ListView):
    model = Monedas
    template_name = 'earn/earn.html'
    context_object_name = 'monedas'
    
class MonedaMainListView(LoginRequiredMixin,ListView):
    model = Monedas
    template_name = 'earn/earn_main.html'
    context_object_name = 'monedas'
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        monedas = self.model.objects.filter(nombre__icontains=nombre)
        return monedas
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario_bus"] = BusquedaMonedas()
        context['nombre'] = self.request.GET.get('nombre', '')
        return context

class AgregarMoneda(LoginRequiredMixin, CreateView):
    model = Monedas
    template_name = 'earn/agregar_monedas.html'
    success_url = reverse_lazy('earn_main')
    fields = ['nombre', 'valor','fecha', 'imagen']
    
class EditarMoneda(LoginRequiredMixin, UpdateView):
    model = Monedas
    template_name = 'earn/editar_monedas.html'
    success_url = reverse_lazy('earn_main')
    fields = ['nombre', 'valor', 'fecha', 'imagen']
    
class VerMoneda(DetailView):
    model = Monedas
    template_name = 'earn/ver_monedas.html'
    
class EliminarMoneda(LoginRequiredMixin, DeleteView):
    model = Monedas
    template_name = 'earn/eliminar_monedas.html'
    success_url = reverse_lazy('earn_main')