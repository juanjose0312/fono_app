from django.urls import path
from .views import Articulacion_como_pronunciar_view
from .views import  Articulacion_seleccion_view
from .views import Articulacion_completar_view

urlpatterns = [
    path(
        'articulacion_pronunciar/',
        Articulacion_como_pronunciar_view.as_view(),
        name='articulacion_como_pronunciar'
    ),
    path(
        'articulacion_completar/<str:letra>/',
        Articulacion_completar_view.as_view(),
        name='articulacion_completar'
    ),
    path(
        'articulacion_seleccion/',
        Articulacion_seleccion_view.as_view(),
        name='articulacion_seleccion'
    ),
]