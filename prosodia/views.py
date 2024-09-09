from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Prosodia_cancion_info
from .models import Prosodia_trabalenguas_info
import random

# Create your views here.
class Prosodia_cancion_view(LoginRequiredMixin, ListView):
    model = Prosodia_cancion_info
    template_name = 'prosodia/prosodia_cancion.html'
    context_object_name = 'instrucciones'

    def get_queryset(self):
        longitud = len(Prosodia_cancion_info.objects.all())
        modulo_seleccionado = random.randint(1, longitud)
        queryset = Prosodia_cancion_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]  
        
        return queryset

class Prosodia_trabalenguas_view(LoginRequiredMixin, ListView):
    model = Prosodia_trabalenguas_info
    template_name = 'prosodia/prosodia_trabalenguas.html'
    context_object_name = 'instrucciones'

    def get_queryset(self):
        longitud = len(Prosodia_trabalenguas_info.objects.all())
        modulo_seleccionado = random.randint(1, longitud)
        queryset = Prosodia_trabalenguas_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]  
        
        return queryset 