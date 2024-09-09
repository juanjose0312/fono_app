from django.urls import path
from .views import Articulacion_como_pronunciar_view
from .views import Articulacion_seleccion_view
from .views import Articulacion_completar_view
from .views import Menu_articulacion_seleccion_view 

urlpatterns = [
    path(
        'articulacion_pronunciar/',
        Articulacion_como_pronunciar_view.as_view(),
        name='articulacion_como_pronunciar'
    ),
    path(
        # para recibir una variable de la url
        'articulacion_completar/<str:letra>/', # letra es la variable que se va a recibir de tipo string
        Articulacion_completar_view.as_view(),
        name='articulacion_completar'
    ),

    path(
        'menu_articulacion_seleccion/', 
        Menu_articulacion_seleccion_view.as_view(), 
        name='menu_articulacion_seleccion'),

    path(
        'articulacion_seleccion/<str:letra>/', # letra es la variable que se va a recibir de tipo string
        Articulacion_seleccion_view.as_view(),
        name='articulacion_seleccion'
    ),

]