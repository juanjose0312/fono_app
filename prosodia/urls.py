from django.urls import path
from .views import Prosodia_cancion_view
from .views import Prosodia_trabalenguas_view

urlpatterns = [
    path(
        'prosodia_cancion/',
        Prosodia_cancion_view.as_view(),
        name='prosodia_cancion'
    ),
    path(
        'prosodia_trabalenguas/',
        Prosodia_trabalenguas_view.as_view(),
        name='prosodia_trabalenguas'
    )
]