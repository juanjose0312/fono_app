from django.db import models

# Create your models here.
class Articulacion_como_pronunciar_info(models.Model):
    nombre= models.TextField(max_length=100, verbose_name="nombre")
    instruciones = models.TextField(max_length=1000, verbose_name="instrucciones_actividad")
    video = models.FileField(upload_to='videos/', null=False, verbose_name="video")
    foto_mayuscula = models.ImageField(upload_to='fotos/', null=False, verbose_name="foto_mayuscula")
    foto_minuscula = models.ImageField(upload_to='fotos/', null=False, verbose_name="foto_minuscula")
    def __str__(self):
        return self.nombre
    
class Articulacion_completar_info(models.Model):
    letra_categoria = models.TextField(max_length=100, verbose_name="letra")
    imagen = models.ImageField(upload_to='fotos/', null=False, verbose_name="imagen")
    texto_incompleto = models.TextField(max_length=30, verbose_name="texto_incompleto")
    texto_completo = models.TextField(max_length=30, verbose_name="texto_completo")
    def __str__(self):

        return self.texto_completo
    
class Articulacion_seleccion_info(models.Model):
    nombre= models.TextField(max_length=100, verbose_name="nombre")
    audio_a = models.FileField(upload_to='audios/', null=False, verbose_name="audio_a")
    audio_e = models.FileField(upload_to='audios/', null=False, verbose_name="audio_e")
    audio_i = models.FileField(upload_to='audios/', null=False, verbose_name="audio_i")
    audio_o = models.FileField(upload_to='audios/', null=False, verbose_name="audio_o")
    audio_u = models.FileField(upload_to='audios/', null=False, verbose_name="audio_u")

    def __str__(self):
        return self.nombre