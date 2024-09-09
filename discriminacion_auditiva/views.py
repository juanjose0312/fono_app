from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Discriminacion_auditiva_escoger_info
from .models import Discriminacion_auditiva_seleccionar_info
import random

# Create your views here.
class Discriminacion_auditiva_escoger_view(LoginRequiredMixin, ListView):
    model = Discriminacion_auditiva_escoger_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_escoger.html'
    context_object_name = 'instrucciones'

    def get_queryset(self):
        # modelo con el que se va a trabajar
        model = Discriminacion_auditiva_escoger_info.objects

        # extrae la longitud
        longitud = len(model.all())

        if longitud < 4:
            return model.all()

        # selecciona 4 numeros aleatorios no repetidos 
        modulos_seleccionados = random.sample(range(1,longitud), 4) 

        # filtra los modulos seleccionados
        queryset = model.filter(id__in=modulos_seleccionados)

        return queryset

class Discriminacion_auditiva_seleccionar_view(LoginRequiredMixin, ListView):
    model = Discriminacion_auditiva_seleccionar_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_seleccionar.html'
    context_object_name = 'instrucciones'
    
    def get_queryset(self):
        # modelo con el que se va a trabajar
        model = Discriminacion_auditiva_seleccionar_info.objects.all()

        lista_model = list(model)

        # extrae la longitud
        longitud = len(lista_model)

        if longitud < 4:
            return model

        # selecciona 4 numeros aleatorios no repetidos 
        modulos_seleccionados = random.sample(range(1,longitud), 4) 

        # filtra los modulos seleccionados
        queryset = [registro for registro in lista_model if registro.id in modulos_seleccionados] 

        # proceso de mezcla de las imagenes
        lista_imagenes = []
        lista_aleatoria = random.sample(range(0,4), 4)

        for registro in queryset:
            lista_imagenes.append(registro.imagen)

        for imagen, orden in zip(lista_imagenes, lista_aleatoria):
            queryset[orden].imagen = imagen

        return queryset

