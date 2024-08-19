from django.contrib import admin
from .models import Discriminacion_auditiva_escoger_info
from .models import Discriminacion_auditiva_seleccionar_info

# Register your models here.
class Discriminacion_auditivaAdmin(admin.ModelAdmin):
    model = Discriminacion_auditiva_escoger_info
    search_fields = ['nombre']

class Discriminacion_auditivaAdmin(admin.ModelAdmin):
    model = Discriminacion_auditiva_seleccionar_info
    search_fields = ['nombre']  

admin.site.register(Discriminacion_auditiva_escoger_info, Discriminacion_auditivaAdmin) 
admin.site.register(Discriminacion_auditiva_seleccionar_info, Discriminacion_auditivaAdmin)



