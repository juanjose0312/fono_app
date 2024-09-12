from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser

# Create your views here.
class PerfilView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'perfil/perfil.html'
    context_object_name = 'users'