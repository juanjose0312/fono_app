from django.db import models

# importa el modelo User de django
from django.contrib.auth.models import User

# Create your models here.
class perfil_info(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_de_idetificacion = models.TextField(max_length=100, verbose_name="Número de identificación")
    nombre = models.TextField(max_length=100, verbose_name="Nombre") 
    apellido = models.TextField(max_length=100, verbose_name="Apellido")
    email = models.TextField(max_length=100, verbose_name="Email")
    fecha_de_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    genero = models.TextField(max_length=100, verbose_name="Género")
    escolaridad = models.TextField(max_length=100, verbose_name="Escolaridad")
    nombre_acudiente = models.TextField(max_length=50, verbose_name="Nombre del acudiente", null=True)
    telefono_acudiente = models.TextField(max_length=20, verbose_name="Teléfono del acudiente", null=True)
    
    def __str__(self):
        return self.numero_de_idetificacion