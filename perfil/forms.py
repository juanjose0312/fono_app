from django import forms
from .models import  perfil_info

class PerfilForm(forms.Form):
    GENDER_CHOICES = [
        ('', 'Seleccione un género'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    ESCOLARIDAD_CHOICES = [
        ('', 'Seleccione un nivel escolar'),
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
    ]

    numero_de_idetificacion = forms.CharField(max_length=100, required=True)
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    #email = forms.EmailField(max_length=100, required=True)
    fecha_de_nacimiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    escolaridad = forms.ChoiceField(choices=ESCOLARIDAD_CHOICES, required=True)
    nombre_acudiente = forms.CharField(max_length=50, required=True)
    telefono_acudiente = forms.CharField(max_length=20, required=True)
    
