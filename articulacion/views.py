
from django.views.generic import ListView #funcion definida en django para listar objetos de la base de datos
from .models import Articulacion_como_pronunciar_info
from .models import Articulacion_completar_info
from .models import Articulacion_seleccion_info

# Create your views here.
class Articulacion_como_pronunciar_view(ListView): #se crea una clase que hereda de ListView
    model = Articulacion_como_pronunciar_info #traer el nombre de como llamamos a la clase que hicimos en models
    template_name = 'articulacion/articulacion_como_pronunciar.html' #traer el nombre de la plantilla html
    context_object_name = 'instrucciones' #traer el nombre de la variable que se va a usar en la plantilla html

class Articulacion_completar_view(ListView): #se crea una clase que hereda de ListView
    model = Articulacion_completar_info #traer el nombre de como llamamos a la clase que hicimos en models
    template_name = 'articulacion/articulacion_completar.html' #traer el nombre de la plantilla html
    context_object_name = 'instrucciones' #traer el nombre de la variable que se va a usar en la plantilla html

    # como obtengo lo que esta llegando en la url
    def get_queryset(self):
        letra = self.kwargs['letra']
        # retorno los objetos de la base de datos que tengan la letra que llega en la url
        return Articulacion_completar_info.objects.filter(letra_categoria=letra)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letra'] = self.kwargs['letra']
        return context
        

class Articulacion_seleccion_view(ListView): #se crea una clase que hereda de ListView
    model = Articulacion_seleccion_info #traer el nombre de como llamamos a la clase que hicimos en models
    template_name = 'articulacion/articulacion_seleccion.html' #traer el nombre de la plantilla html
    context_object_name = 'instrucciones' #traer el nombre de la variable que se va a usar en la plantilla html