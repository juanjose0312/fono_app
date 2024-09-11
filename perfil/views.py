from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
class PerfilView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'perfil/perfil.html'
    context_object_name = 'users'