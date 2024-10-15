from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import random

from .models import Discriminacion_auditiva_escoger_info
from .models import Discriminacion_auditiva_seleccionar_info


# Create your views here.
class Discriminacion_auditiva_escoger_view(LoginRequiredMixin, ListView):
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_escoger.html'
    context_object_name = 'instrucciones'

    def generate_queryset(self):
        model = Discriminacion_auditiva_escoger_info.objects
        longitud = len(model.all())
        if longitud < 4:
            return model.all()
        else:
            modulos_seleccionados = random.sample(range(1, longitud + 1), 4)
            return model.filter(id__in=modulos_seleccionados)

    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            self._queryset = self.generate_queryset()
        return self._queryset

    def post(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        respuestas = []
        for key, value in request.POST.items():
            if key.startswith('respuesta_'):
                
                key = int(key.split('_')[1])
                imagen_correcta = self.queryset[key-1].imagen_correcta.url

                if imagen_correcta == value:
                    respuestas.append({
                        'respuesta': True,
                        'imagen': value
                    })
                else:
                    respuestas.append({
                        'respuesta': False,
                        'imagen': value
                    })

        return render(request, 'discriminacion_auditiva/discriminacion_auditiva_escoger_respuesta.html', {'resultados': respuestas})

class Discriminacion_auditiva_seleccionar_view(LoginRequiredMixin, ListView):
    model = Discriminacion_auditiva_seleccionar_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_seleccionar.html'
    context_object_name = 'instrucciones'
    
    def generate_queryset(self):
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

        return queryset
    
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            self._queryset = self.generate_queryset()
        return self._queryset

    def post(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        respuestas = []
        for key, value in request.POST.items():
            if key.startswith('respuesta_'):
                
                key = int(key.split('_')[1])
                imagen_correcta = self.queryset[key-1].imagen.url

                if imagen_correcta == value:
                    respuestas.append({
                        'respuesta': True,
                        'imagen': value
                    })
                else:
                    respuestas.append({
                        'respuesta': False,
                        'imagen': value
                    })

        return render(request, 'discriminacion_auditiva/discriminacion_auditiva_escoger_respuesta.html', {'resultados': respuestas})

