from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField
    gendet = models.CharField(max_length=30)
    escolaridad = models.CharField(max_length=40)

    def __str__(self):
        return self.username.username