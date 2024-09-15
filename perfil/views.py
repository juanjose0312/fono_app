from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.
class PerfilView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'perfil/perfil.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
