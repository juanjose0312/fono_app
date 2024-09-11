from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    usernmae = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    GENDER_CHOICES = [
        ('', 'Seleccione un género'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
     ]   
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    ESCOLARIDAD_CHOICES = [
        ('', 'Seleccione un nivel escolar'),
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
    ]
    escolaridad = forms.ChoiceField(choices=ESCOLARIDAD_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',  'gender', 'escolaridad', 'password1', 'password2', 'date_of_birth')