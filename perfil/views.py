from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.shortcuts import render
from django.views import View
from .models import perfil_info
from .forms import PerfilForm
from django.urls import reverse_lazy
# importa la función reverse_lazy para redireccionar el flujo a una url

# Create your views here.
class PerfilView(LoginRequiredMixin, View):
    template_name = 'perfil/perfil.html'
    context_object_name = 'users'

    def get(self, request):
        user = User.objects.filter(username=self.request.user.username).first()
        
        perfil = perfil_info.objects.filter(username=user).first()
        if perfil:
            return render(request, self.template_name, {'perfil': perfil})
        else:
            return render(request, 'perfil/perfil_sin_datos.html', {'error': 'Perfil no encontrado'})

# view de un formulario de perfil
class PerfilFormView(LoginRequiredMixin, FormView):
    #model = perfil_info
    form_class = PerfilForm
    template_name = 'perfil/perfil_formulario.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        user = User.objects.filter(username=self.request.user.username).first()
        perfil = perfil_info.objects.filter(username=user).first()
        if perfil:
            perfil.numero_de_idetificacion = form.cleaned_data['numero_de_idetificacion']
            perfil.nombre = form.cleaned_data['nombre']
            perfil.apellido = form.cleaned_data['apellido']
            perfil.email = form.cleaned_data['email']
            perfil.fecha_de_nacimiento = form.cleaned_data['fecha_de_nacimiento']
            perfil.genero = form.cleaned_data['genero']
            perfil.escolaridad = form.cleaned_data['escolaridad']
            perfil.nombre_acudiente = form.cleaned_data['nombre_acudiente']
            perfil.telefono_acudiente = form.cleaned_data['telefono_acudiente']
            perfil.save()
        else:
            perfil = perfil_info(
                username=user,
                numero_de_idetificacion=form.cleaned_data['numero_de_idetificacion'],
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                fecha_de_nacimiento=form.cleaned_data['fecha_de_nacimiento'],
                genero=form.cleaned_data['genero'],
                escolaridad=form.cleaned_data['escolaridad'],
                nombre_acudiente = form.cleaned_data['nombre_acudiente'], 
                telefono_acudiente = form.cleaned_data['telefono_acudiente'],
            )
            perfil.save()
        return super().form_valid(form)