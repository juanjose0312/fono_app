from django.contrib import admin
from .models import Discriminacion_auditiva_info

# Register your models here.
class Discriminacion_auditivaAdmin(admin.ModelAdmin):
    model = Discriminacion_auditiva_info



admin.site.register(Discriminacion_auditiva_info, Discriminacion_auditivaAdmin)