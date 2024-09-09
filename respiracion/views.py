# se importa un padre de las vistas genericas de django
# que funciona para listar objetos de la base de datos
import random
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Respiracion_info #importar la clase que hicimos en models

# Create your views here.
class Respiracion_view(LoginRequiredMixin, ListView): #se crea una clase que hereda de ListView
    model = Respiracion_info #traer el nombre de como llamamos a la clase que hicimos en models
    template_name = 'respiracion/respiracion.html' #traer el nombre de la plantilla html
    context_object_name = 'instrucciones' #traer el nombre de la variable que se va a usar en la plantilla html

    def get_queryset(self):
        longitud = len(Respiracion_info.objects.all())
        modulo_seleccionado = random.randint(1, longitud)
        queryset = Respiracion_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]  
        
        return queryset