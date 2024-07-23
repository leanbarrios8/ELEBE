from django.urls import path   
from .import views 

urlpatterns = [
    path('earn/', views.MonedaListView.as_view(), name ='earn'),
    path('earn_main/', views.MonedaMainListView.as_view(), name ='earn_main'),
    path('earn/agregar/', views.AgregarMoneda.as_view(), name ='agregar_monedas'),
    path('earn/<int:pk>/', views.VerMoneda.as_view(), name ='ver_monedas'),
    path('earn/<int:pk>/editar/', views.EditarMoneda.as_view(), name ='editar_monedas'),
    path('earn/<int:pk>/eliminar/', views.EliminarMoneda.as_view(), name ='eliminar_monedas'),
]
