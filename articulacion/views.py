from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.views.generic import ListView #funcion definida en django para listar objetos de la base de datos
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import random
from django.shortcuts import render

from .models import (
    Articulacion_como_pronunciar_info,
    Articulacion_completar_info,
    Articulacion_seleccion_info
)

def audio_a_texto(audio_file):
        """"
        Función para convertir un archivo de audio a texto.

        Parámetros:
            audio_file: Archivo de audio a convertir.
        """
        audio = AudioSegment.from_file(BytesIO(audio_file.read()))
        audio_path = 'grabacion.wav'
        audio.export(audio_path, format='wav')

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            try:
                result = recognizer.recognize_google(audio_data, language='es-CO').lower()
                estado = True

            except sr.UnknownValueError:
                result = "No se pudo entender el audio."
                estado = False

            except sr.RequestError as e:
                result = "Errorr al conectar con el servicio de reconocimiento de voz."
                estado = False
        
        return result, estado


# Create your views here.
class Menu_articulacion_como_pronunciar_view(LoginRequiredMixin, ListView):
    model = Articulacion_como_pronunciar_info 
    template_name = 'articulacion/menu_articulacion_como_pronunciar.html'
    context_object_name = 'instrucciones'

class Articulacion_como_pronunciar_view(LoginRequiredMixin, ListView):
    model = Articulacion_como_pronunciar_info 
    template_name = 'articulacion/articulacion_como_pronunciar.html'
    context_object_name = 'instrucciones'

     # se encarga de generar el queryset que se va a mostrar en la plantilla (iterable)
    def get_queryset(self):
        # asigna a la variable letra el valor que llega en la url
        letra = self.kwargs['letra']
        # retorno los objetos de la base de datos que tengan la letra que llega en la url
        return Articulacion_como_pronunciar_info.objects.filter(nombre=letra)

    # se agrega una variable mas al contexto que se va a enviar a el template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letra'] = self.kwargs['letra']
        return context

class Menu_articulacion_completar_view(LoginRequiredMixin, ListView):
    model = Articulacion_completar_info 
    template_name = 'articulacion/menu_articulacion_completar.html'
    context_object_name = 'instrucciones' 

class Articulacion_completar_view(APIView):

    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        self.letra = kwargs.get('letra')
        self.queryset = Articulacion_completar_info.objects.filter(letra_categoria=self.letra)
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):

        # Contexto para pasar al template
        context = {
            'instrucciones': self.queryset
        }
        
        # Renderiza el template HTML con el contexto
        return render(request, 'articulacion/articulacion_completar.html', context)
    
    def post(self, request, *args, **kwargs):
        if 'audio' not in request.FILES:
            return Response({'result': 'No se recibió ningún archivo de audio.'}, status=status.HTTP_400_BAD_REQUEST)
        if 'idbutton' not in request.POST:
            return Response({'result': 'No se recibió ningún id de botón.'}, status=status.HTTP_400_BAD_REQUEST)

        # Leer el archivo de audio desde la solicitud
        audio_file = request.FILES['audio']
        idbutton = request.POST['idbutton']

        # Palabra objetivo para verificar
        num_parrafo = idbutton.split('_')[1]
        palabra_correcta = self.queryset[int(num_parrafo)-1].texto_completo
        palabra_audio, estado = audio_a_texto(audio_file)
        
        if estado:
            if palabra_audio == palabra_correcta.lower():
                # Verificar si el texto es igual a la palabra objetivo
                result = "¡Correcto!"
            else:
                # Si el texto no es igual a la palabra objetivo
                result = f"¡Incorrecto! dijiste {palabra_audio}"
        else:
            # Si no se pudo entender el audio o fallo el servidor de reconocimiento de voz
            result = palabra_audio

        return Response({'result': result})

class Menu_articulacion_seleccion_view(LoginRequiredMixin,ListView):
    model = Articulacion_seleccion_info 
    template_name = 'articulacion/menu_articulacion_seleccion.html'
    context_object_name = 'instrucciones' 

class Articulacion_seleccion_view(LoginRequiredMixin, ListView):
    model = Articulacion_seleccion_info 
    template_name = 'articulacion/articulacion_seleccion.html'
    context_object_name = 'instrucciones' 

    def generate_queryset(self):
        # asigna a la variable letra el valor que llega en la url
        letra = self.kwargs['letra']
        # retorno los objetos de la base de datos que tengan la letra que llega en la url
        audios = Articulacion_seleccion_info.objects.filter(letra_categoria=letra)[0]
        audios = [
            {
                'audio':audios.audio_a.url,
                'respuesta':'a'
            },
            { 
                'audio':audios.audio_e.url,
                'respuesta':'e'
            },
            { 
                'audio':audios.audio_i.url,
                'respuesta':'i'
            },
            { 
                'audio':audios.audio_o.url,
                'respuesta':'o'
            },
            { 
                'audio':audios.audio_u.url,
                'respuesta':'u'
            },
            ]
        
        return audios
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        letra = self.kwargs['letra']
        vocales = ['a','e','i','o','u']
        context['letra'] = letra
        context['silabas'] = [f'{letra}{vocal}' for vocal in vocales]
        return context
    
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            self._queryset = self.generate_queryset()
        return self._queryset

    def post(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        respuestas = []
        for key, value in request.POST.items():
            if key.startswith('respuesta_'):
                
                key = key.split('_')[1]

                diccionario = {
                        'correcto': key,
                        'eleccion': value
                }

                if key == value:
                    diccionario['respuesta'] = True
                else:
                    diccionario['respuesta'] = False

                respuestas.append(diccionario)

        return render(request, 'articulacion/articulacion_seleccion_respuesta.html', {'resultados': respuestas})