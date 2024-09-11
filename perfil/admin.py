from django.contrib import admin
from users.models import Perfil

# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    model = Perfil
    list_display = ('username','email','first_name','last_name','date_of_birth','gendet','escolaridad')

admin.site.register(Perfil, PerfilAdmin)








