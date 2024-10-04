from django.db import models

# Create your models here.
class Discriminacion_auditiva_escoger_info(models.Model):
    nombre= models.TextField(max_length=100, verbose_name="nombre")
    imagen_correcta = models.ImageField(upload_to='fotos/', null=False, verbose_name="imagen_correcta")
    imagen_incorrecta = models.ImageField(upload_to='fotos/', null=False, verbose_name="imagen_incorrecta")
    audio  = models.FileField(upload_to='audios/', null=False, verbose_name="audio")

    def __str__(self):
        return self.nombre
    
    def es_imagen_correcta(self, imagen_url):
        return self.imagen_correcta.url == imagen_url

    
class Discriminacion_auditiva_seleccionar_info(models.Model):
    nombre= models.TextField(max_length=100, verbose_name="nombre")
    imagen = models.ImageField(upload_to='fotos/', null=False, verbose_name="imagen")
    audio  = models.FileField(upload_to='audios/', null=False, verbose_name="audio")

    def __str__(self):
        return self.nombre 