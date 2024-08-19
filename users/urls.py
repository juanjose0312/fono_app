from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(template_name="users/login.html"), 
        name="login"  # Añadir el nombre de la ruta
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
]