from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirige a la página de inicio o donde prefieras

#    def form_valid(self, form):
#        user = form.save()
#        username = form.cleaned_data.get('username')
#        password = form.cleaned_data.get('password1')
#        user = authenticate(username=username, password=password)
#        login(self.request, user)
#
#        return super().form_valid(form)

class ProfileView(ListView):
    template_name = 'users/profile.html'
    model = User
    context_object_name = 'users'