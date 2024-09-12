from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm

class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)