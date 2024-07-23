from django.urls import path   
from .import views 

urlpatterns = [
    path('about/', views.EstudiosListView.as_view(), name ='about'),
    path('about/agregar/', views.AgregarEstudio.as_view(), name ='agregar_estudios'),
    path('about/<int:pk>/', views.VerEstudio.as_view(), name ='ver_estudios'),
    path('about/<int:pk>/editar/', views.EditarEstudio.as_view(), name ='editar_estudios'),
    path('about/<int:pk>/eliminar/', views.EliminarEstudio.as_view(), name ='eliminar_estudios'),
]
