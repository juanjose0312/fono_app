from django.urls import path
from .views import PerfilView, PerfilFormView


urlpatterns = [
    path('perfil/', PerfilView.as_view(), name='perfil'),
     path('perfil/perfil_formulario/', PerfilFormView.as_view(), name='perfil_formulario'),
    #path('perfil_formulario/', PerfilFormView.as_view(), name='perfil_formulario'),
]
