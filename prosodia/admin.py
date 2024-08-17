from django.contrib import admin
from .models import Prosodia_cancion_info, Prosodia_trabalenguas_info

# Register your models here.

class Prosodia_cancionAdmin(admin.ModelAdmin):
    model = Prosodia_cancion_info

    search_fields = ['nombre']

class Prosodia_trabalenguasAdmin(admin.ModelAdmin):
    model = Prosodia_trabalenguas_info
    search_fields = ['nombre']


admin.site.register(Prosodia_cancion_info, Prosodia_cancionAdmin)
admin.site.register(Prosodia_trabalenguas_info, Prosodia_trabalenguasAdmin)
