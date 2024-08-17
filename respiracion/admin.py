from django.contrib import admin
from .models import Respiracion_info # importar los modelos de la categorias

# Register your models here.
class RespiracionAdmin(admin.ModelAdmin):
    model = Respiracion_info #llamamos el modelo 
    list_display = ('nombre', 'instrucciones', 'video') # la caracteristicas que se mostraran en el panel de administracion
    search_fields = ['nombre'] # campo de busqueda que va aparecer en el panel de administracion
admin.site.register(Respiracion_info, RespiracionAdmin) # registramos el modelo