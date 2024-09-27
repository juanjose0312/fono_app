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

    numero_de_idetificacion = forms.CharField(max_length=100, required=False)
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, required=False)
    fecha_de_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    escolaridad = forms.ChoiceField(choices=ESCOLARIDAD_CHOICES, required=True)
    nombre_acudiente = forms.CharField(max_length=50, required=False)
    telefono_acudiente = forms.CharField(max_length=20, required=False)
    


    #class Meta:
        #model = perfil_info
        #fields = (
        #    'numero_de_idetificacion',
        #    'fecha_de_nacimiento',
        #    'numero_de_idetificacion',
        #    'nombre',
        #    'apellido',
        #    'email',
        #    'fecha_de_nacimiento',
        #    'genero',
        #    'escolaridad',
    #    )