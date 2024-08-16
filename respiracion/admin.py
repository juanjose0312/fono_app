from django.contrib import admin
from .models import Respiracion_info

# Register your models here.
class RespiracionAdmin(admin.ModelAdmin):
    model = Respiracion_info

admin.site.register(Respiracion_info, RespiracionAdmin)