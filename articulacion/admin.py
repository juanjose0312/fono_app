from django.contrib import admin
from .models import Articulacion_como_pronunciar_info, Articulacion_completar_info, Articulacion_seleccion_info

# Register your models here.
class Articulacion_como_pronunciarAdmin(admin.ModelAdmin):
    model = Articulacion_como_pronunciar_info
    list_display = ('nombre', 'instruciones', 'video', 'foto_mayuscula', 'foto_minuscula')
    search_fields = ['nombre']

class Articulacion_completarAdmin(admin.ModelAdmin):
    model = Articulacion_completar_info
    list_display = ('letra_categoria', 'imagen', 'texto_incompleto', 'texto_completo')
    search_fields = ['letra_categoria', 'texto_completo']

class Articulacion_seleccionAdmin(admin.ModelAdmin):
    model = Articulacion_seleccion_info
    list_display = ('nombre', 'audio_a', 'audio_e', 'audio_i', 'audio_o', 'audio_u')
    search_fields = ['nombre']

admin.site.register(Articulacion_como_pronunciar_info, Articulacion_como_pronunciarAdmin)
admin.site.register(Articulacion_completar_info, Articulacion_completarAdmin)
admin.site.register(Articulacion_seleccion_info, Articulacion_seleccionAdmin)

