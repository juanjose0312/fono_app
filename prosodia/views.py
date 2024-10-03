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
        self.modulo_seleccionado = random.randint(
            1,
            Prosodia_cancion_info.objects.count()
        )
        
    
    def get(self, request, format=None):
        queryset = Prosodia_cancion_info.objects.all()[self.modulo_seleccionado-1:self.modulo_seleccionado]
        # Contexto para pasar al template
        context = {
            'instrucciones': queryset
        }
        
        # Renderiza el template HTML con el contexto
        return render(request, 'prosodia/prosodia_cancion.html', context)
    
    def post(self, request, *args, **kwargs):
        if 'audio' not in request.FILES:
            return Response({'result': 'No se recibió ningún archivo de audio.'}, status=status.HTTP_400_BAD_REQUEST)
        if 'idbutton' not in request.POST:
            return Response({'result': 'No se recibió ningún id de botón.'}, status=status.HTTP_400_BAD_REQUEST)

        # Leer el archivo de audio desde la solicitud
        audio_file = request.FILES['audio']
        idbutton = request.POST['idbutton']
        
        # Convertir el archivo de audio a formato compatible con SpeechRecognition
        audio = AudioSegment.from_file(BytesIO(audio_file.read()))
        audio_path = 'grabacion.wav'
        audio.export(audio_path, format='wav')

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            try:
                # Realizar reconocimiento de voz
                texto = recognizer.recognize_google(audio_data, language='es-ES') 

                # Palabra objetivo para verificar
                num_parrafo = idbutton.split('_')[1]
                query_set = list(Prosodia_cancion_info.objects.all()[self.modulo_seleccionado-1:self.modulo_seleccionado])
                query = getattr(query_set[0], f'respuesta_{num_parrafo}')

                palabra_objetivo = query
                if texto.lower() == palabra_objetivo.lower():
                    result = "Exitoso"
                else:
                    result = f"Incorrecto. Usted dijo: '{texto}', pero la palabra correcta es: '{palabra_objetivo}'"
            
            except sr.UnknownValueError:
                result = "No se pudo entender el audio."
            except sr.RequestError as e:
                result = f"Error al conectar con el servicio de reconocimiento de voz: {e}"

        return Response({'result': result})

class ProsodiaTrabalenguasAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        longitud = Prosodia_trabalenguas_info.objects.count()
        modulo_seleccionado = random.randint(1, longitud)
        queryset = Prosodia_trabalenguas_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]
        serializer = ProsodiaTrabalenguasInfoSerializer(queryset, many=True)
        return Response(serializer.data)