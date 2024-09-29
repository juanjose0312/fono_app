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

## Create your views here.
#class Prosodia_cancion_view(LoginRequiredMixin, ListView):
#    model = Prosodia_cancion_info
#    template_name = 'prosodia/prosodia_cancion.html'
#    context_object_name = 'instrucciones'
#
#    def get_queryset(self):
#        longitud = len(Prosodia_cancion_info.objects.all())
#        modulo_seleccionado = random.randint(1, longitud)
#        queryset = Prosodia_cancion_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]  
#        
#        return queryset
    
class ProsodiaCancionAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        longitud = Prosodia_cancion_info.objects.count()
        modulo_seleccionado = random.randint(1, longitud)
        queryset = Prosodia_cancion_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]
        # Contexto para pasar al template
        context = {
            'instrucciones': queryset
        }
        
        # Renderiza el template HTML con el contexto
        return render(request, 'prosodia/prosodia_cancion.html', context)
    
    def post(self, request, *args, **kwargs):
        if 'audio' not in request.FILES:
            return Response({'result': 'No se recibió ningún archivo de audio.'}, status=status.HTTP_400_BAD_REQUEST)

        # Leer el archivo de audio desde la solicitud
        audio_file = request.FILES['audio']
        
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
                print(f"Texto reconocido: {texto}")

                # Palabra objetivo para verificar
                palabra_objetivo = "hola"
                if texto.lower() == palabra_objetivo.lower():
                    result = "Exitoso"
                else:
                    result = f"Incorrecto. Usted dijo: '{texto}', pero la palabra correcta es: '{palabra_objetivo}'"
            
            except sr.UnknownValueError:
                result = "No se pudo entender el audio."
            except sr.RequestError as e:
                result = f"Error al conectar con el servicio de reconocimiento de voz: {e}"

        return Response({'result': result})

#class Prosodia_trabalenguas_view(LoginRequiredMixin, ListView):
#    model = Prosodia_trabalenguas_info
#    template_name = 'prosodia/prosodia_trabalenguas.html'
#    context_object_name = 'instrucciones'
#
#    def get_queryset(self):
#        longitud = len(Prosodia_trabalenguas_info.objects.all())
#        modulo_seleccionado = random.randint(1, longitud)
#        queryset = Prosodia_trabalenguas_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]  
#        
#        return queryset 

class ProsodiaTrabalenguasAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        longitud = Prosodia_trabalenguas_info.objects.count()
        modulo_seleccionado = random.randint(1, longitud)
        queryset = Prosodia_trabalenguas_info.objects.all()[modulo_seleccionado-1:modulo_seleccionado]
        serializer = ProsodiaTrabalenguasInfoSerializer(queryset, many=True)
        return Response(serializer.data)