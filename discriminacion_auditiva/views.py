from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Discriminacion_auditiva_escoger_info
from .models import Discriminacion_auditiva_seleccionar_info

# Create your views here.
class Discriminacion_auditiva_escoger_view(LoginRequiredMixin, ListView):
    model = Discriminacion_auditiva_escoger_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_escoger.html'
    context_object_name = 'instrucciones'

class Discriminacion_auditiva_seleccionar_view(LoginRequiredMixin, ListView):
    model = Discriminacion_auditiva_seleccionar_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_seleccionar.html'
    context_object_name = 'instrucciones'

