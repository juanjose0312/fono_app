from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


#class CustomUserCreationForm(UserCreationForm):
#    GENDER_CHOICES = [
#        ('', 'Seleccione un género'),
#        ('M', 'Masculino'),
#        ('F', 'Femenino'),
#        ('O', 'Otro'),
#    ]
#    ESCOLARIDAD_CHOICES = [
#        ('', 'Seleccione un nivel escolar'),
#        ('1', 'Primero'),
#        ('2', 'Segundo'),
#        ('3', 'Tercero'),
#        ('4', 'Cuarto'),
#        ('5', 'Quinto'),
#    ]
#    
#    fecha_de_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
#    genero = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
#    escolaridad = forms.ChoiceField(choices=ESCOLARIDAD_CHOICES, required=True)
#    numero_de_identificacion = forms.CharField(max_length=20, required=False)
#    nombre_acudiente = forms.CharField(max_length=50, required=False)
#    telefono_acudiente = forms.CharField(max_length=20, required=False)
#
#    class Meta:
#        model = CustomUser
#        fields = ('username', 'email', 'password1', 'password2', 'fecha_de_nacimiento', 'genero', 'escolaridad', 'numero_de_identificacion', 'nombre_acudiente', 'telefono_acudiente')