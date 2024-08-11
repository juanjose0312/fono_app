from django.db import models

# Create your models here.
class Respiracion_info(models.Model):
    nombre= models.TextField(max_length=100, verbose_name="nombre")
    instrucciones = models.TextField(max_length=1000, verbose_name="instrucciones_actividad")
    video = models.FileField(upload_to='videos/', null=False, verbose_name="video")

    def __str__(self):
        return self.nombre