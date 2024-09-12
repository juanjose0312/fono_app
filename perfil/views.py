from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser

# Create your views here.
class PerfilView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'perfil/perfil.html'
    context_object_name = 'users'

    def get_queryset(self):
        print(f'{CustomUser.objects.filter(username=self.request.user.username)}')
        print('hola')
        return CustomUser.objects.filter(username=self.request.user.username)
