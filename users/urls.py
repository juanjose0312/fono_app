from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path(
        '', 
        LoginView.as_view(template_name="users/login.html"), 
        name="login"  # Añadir el nombre de la ruta
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', RegisterView.as_view(), name='registro'),
]