from django.views.generic import ListView
from .models import Discriminacion_auditiva_info

# Create your views here.
class Discriminacion_auditiva_escoger_view(ListView):
    model = Discriminacion_auditiva_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_escoger.html'
    context_object_name = 'instrucciones'

class Discriminacion_auditiva_seleccionar_view(ListView):
    model = Discriminacion_auditiva_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_seleccionar.html'
    context_object_name = 'instrucciones'

