from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import random
from django.shortcuts import render

from .models import Prosodia_cancion_info, Prosodia_trabalenguas_info
from .serializer import ProsodiaCancionInfoSerializer, ProsodiaTrabalenguasInfoSerializer
    
class ProsodiaCancionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cantidad_modulos = Prosodia_cancion_info.objects.count()
        modulo_numero = random.randint(1,cantidad_modulos)
        self.queryset = Prosodia_cancion_info.objects.all()[modulo_numero-1:modulo_numero]
        
    
    def get(self, request, format=None):
        
        # Contexto para pasar al template
        context = {
            'instrucciones': self.queryset
        }
        
        # Renderiza el template HTML con el contexto
        return render(request, 'prosodia/prosodia_cancion.html', context)
    
    def audio_a_texto(self, audio_file):
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
        palabra_correcta = getattr(self.queryset[0], f'respuesta_{num_parrafo}')
        palabra_audio, estado = self.audio_a_texto(audio_file)
        
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

class ProsodiaTrabalenguasAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        longitud = Prosodia_trabalenguas_info.objects.count()
        modulo_seleccionado = random.randint(1, longitud)
        queryset = Prosodia_trabalenguas_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]
        serializer = ProsodiaTrabalenguasInfoSerializer(queryset, many=True)
        return Response(serializer.data)