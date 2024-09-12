from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=30, null=True)
    escolaridad = models.CharField(max_length=40, null=True)
    numero_de_identificacion = models.CharField(max_length=20, null=True)
    nombre_acudiente = models.CharField(max_length=50, null=True)
    telefono_acudiente = models.CharField(max_length=20, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Cambia el related_name para evitar conflictos
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Cambia el related_name para evitar conflictos
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )