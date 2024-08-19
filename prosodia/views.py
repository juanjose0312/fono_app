from django.views.generic import ListView
from .models import Prosodia_cancion_info
from .models import Prosodia_trabalenguas_info

# Create your views here.
class Prosodia_cancion_view(ListView):
    model = Prosodia_cancion_info
    template_name = 'prosodia/prosodia_cancion.html'
    context_object_name = 'instrucciones'

class Prosodia_trabalenguas_view(ListView):
    model = Prosodia_trabalenguas_info
    template_name = 'prosodia/prosodia_trabalenguas.html'
    context_object_name = 'instrucciones'
