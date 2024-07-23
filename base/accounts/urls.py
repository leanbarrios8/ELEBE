from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from .import views 

urlpatterns = [
    path('login/', views.login, name="login"),
    path('sign_up/', views.registro, name="sign_up"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('ver_perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('editar_perfil/password/', views.CambiarPassword.as_view(), name='cambiar_contra'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)