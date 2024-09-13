from django.views.generic import TemplateView
import random

# Create your views here.
def ubicacion_notas():
    # funcion que genera el contexto que va a pasar a la vista
    lista_random = []
    cadena = ""
    tabla_homologada_notas = {
        '0':'do',
        '1':'re',
        '2':'mi',
        '3':'fa',
        '4':'sol',
        '5':'la',
        '6':'si',
    }
    
    for i in range(6):
        numero = random.randint(0,6)
        nota = tabla_homologada_notas[str(numero)]
        cadena += nota + " "

        lista_random.append([
            numero,
            nota
            ])
        
    cadena = cadena.strip()

    return lista_random, cadena

class ResonanciaView(TemplateView):
    template_name = 'resonancia/resonancia.html'
    context_object_name = 'notas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lista_random, cadena = ubicacion_notas()
        context['notas'] = lista_random
        context['cadena'] = cadena
        context['range'] = range(7)
        return context