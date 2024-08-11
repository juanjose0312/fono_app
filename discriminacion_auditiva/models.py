from django.db import models

# Create your models here.
class Discriminacion_auditiva_info(models.Model):
    nombre= models.TextField(max_length=100, verbose_name="nombre")
    imagen = models.ImageField(upload_to='fotos/', null=False, verbose_name="imagen")
    audio  = models.FileField(upload_to='audios/', null=False, verbose_name="audio")

    def __str__(self):
        return self.nombre