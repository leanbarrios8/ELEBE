from django import forms
from django.views.generic.edit import CreateView
from .models import Monedas

class AgregarMonedasModificado(CreateView):
    nombre = forms.CharField(max_length=20, help_text="Ingrese el nombre de la moneda.")
    valor = forms.CharField(max_length=20, help_text="Ingrese el valor de la moneda.")
    fecha = forms.DateField()
    imagen = forms.ImageField(label="Imagen de la moneda", help_text="Suba una imagen representativa de la moneda.")

class BusquedaMonedas(forms.Form):
    nombre = forms.CharField(max_length=20)