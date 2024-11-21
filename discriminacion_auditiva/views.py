from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Min

import random

from .models import Discriminacion_auditiva_escoger_info
from .models import Discriminacion_auditiva_seleccionar_info


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
                instruccion = self.queryset[key-1]
                imagen_correcta = instruccion.imagen_correcta.url

                if imagen_correcta == value:
                    respuestas.append({
                        'respuesta': True,
                        'imagen_usuario': value,
                        'imagen_correcta': imagen_correcta
                    })
                else:
                    respuestas.append({
                        'respuesta': False,
                        'imagen_usuario': value,
                        'imagen_correcta': imagen_correcta
                    })

        return render(request, 'discriminacion_auditiva/discriminacion_auditiva_escoger_respuesta.html', {'resultados': respuestas})

class Discriminacion_auditiva_seleccionar_view(LoginRequiredMixin, ListView):
    model = Discriminacion_auditiva_seleccionar_info
    template_name = 'discriminacion_auditiva/discriminacion_auditiva_seleccionar.html'
    context_object_name = 'instrucciones'
    
    def generate_queryset(self):
        # modelo con el que se va a trabajar
        model = Discriminacion_auditiva_seleccionar_info.objects.all()
        min_id = model.aggregate(Min('id'))['id__min']

        lista_model = list(model)

        # extrae la longitud
        longitud = len(lista_model)

        if longitud < 4:
            return model

        # selecciona 4 numeros aleatorios no repetidos 
        modulos_seleccionados = random.sample(range(min_id,(min_id + longitud )), 4) 
        desorden_de_lista = random.sample(range(4), 4)

        # filtra los modulos seleccionados
        queryset_ordenado = [registro for registro in lista_model if registro.id in modulos_seleccionados] 
        queryset= queryset_ordenado.copy()
        for objeto, index in zip(queryset_ordenado, desorden_de_lista):
            queryset[index] = objeto

        queryset_imagenes = []
        for objeto in queryset_ordenado :
            queryset_imagenes.append(objeto.imagen)

        queryset_dic = {
            'informacion' : queryset,
            'imagenes' : queryset_imagenes, 
        }
       
        return queryset_dic
    
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            self._queryset = self.generate_queryset()
        return self._queryset

    def post(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        respuestas = []
        for key, value in request.POST.items():
            if key.startswith('respuesta_'):
                
                imagen_seleccionada, imagen_correcta = value.split(',')
                              
                if imagen_correcta == imagen_seleccionada:
                    respuestas.append({
                        'respuesta': True,
                        'imagen_correcta': imagen_correcta,
                        'imagen_seleccionada': imagen_seleccionada 
                    })
                else:
                    respuestas.append({
                        'respuesta': False,
                        'imagen_correcta': imagen_correcta,
                        'imagen_seleccionada': imagen_seleccionada 
                    })

                
        return render(request, 'discriminacion_auditiva/discriminacion_auditiva_seleccionar_respuesta.html', {'resultados': respuestas})

